from pathlib import Path
import shutil
import config
from utils import (
    pdfs_to_markdowns, 
    clear_directory_contents, 
    docx_to_markdown, 
    csv_to_markdown, 
    txt_to_markdown, 
    url_to_markdown
)

class DocumentManager:

    def __init__(self, rag_system):
        self.rag_system = rag_system
        self.markdown_dir = Path(config.MARKDOWN_DIR)
        self.markdown_dir.mkdir(parents=True, exist_ok=True)
        
    def add_documents(self, document_paths, progress_callback=None):
        if not document_paths:
            return 0, 0
            
        document_paths = [document_paths] if isinstance(document_paths, str) else document_paths
        supported_suffixes = {".pdf", ".md", ".docx", ".csv", ".txt"}
        document_paths = [p for p in document_paths if p and Path(p).suffix.lower() in supported_suffixes]
        
        if not document_paths:
            return 0, 0
            
        added = 0
        skipped = 0
            
        for i, doc_path in enumerate(document_paths):
            if progress_callback:
                progress_callback((i + 1) / len(document_paths), f"Processing {Path(doc_path).name}")
                
            doc_name = Path(doc_path).name  # E.g. "report.docx"
            md_path = self.markdown_dir / f"{doc_name}.md"  # E.g. "report.docx.md"
            
            if md_path.exists():
                skipped += 1
                continue
                
            try:            
                suffix = Path(doc_path).suffix.lower()
                if suffix == ".md":
                    shutil.copy(doc_path, md_path)
                elif suffix == ".docx":
                    docx_to_markdown(doc_path, self.markdown_dir)
                    temp_md = self.markdown_dir / f"{Path(doc_path).stem}.md"
                    if temp_md.exists():
                        temp_md.rename(md_path)
                elif suffix == ".csv":
                    csv_to_markdown(doc_path, self.markdown_dir)
                    temp_md = self.markdown_dir / f"{Path(doc_path).stem}.md"
                    if temp_md.exists():
                        temp_md.rename(md_path)
                elif suffix == ".txt":
                    txt_to_markdown(doc_path, self.markdown_dir)
                    temp_md = self.markdown_dir / f"{Path(doc_path).stem}.md"
                    if temp_md.exists():
                        temp_md.rename(md_path)
                elif suffix == ".pdf":
                    pdfs_to_markdowns(str(doc_path), overwrite=False)            
                    temp_md = self.markdown_dir / f"{Path(doc_path).stem}.md"
                    if temp_md.exists():
                        temp_md.rename(md_path)
                else:
                    skipped += 1
                    continue
                
                parent_chunks, child_chunks = self.rag_system.chunker.create_chunks_single(md_path)
                
                if not child_chunks:
                    skipped += 1
                    continue
                
                collection = self.rag_system.vector_db.get_collection(self.rag_system.collection_name)
                collection.add_documents(child_chunks)
                self.rag_system.parent_store.save_many(parent_chunks)
                
                added += 1
                
            except Exception as e:
                print(f"Error processing {doc_path}: {e}")
                skipped += 1
            
        return added, skipped
        
    def add_url(self, url):
        try:
            safe_name = url_to_markdown(url, self.markdown_dir)
            md_path = self.markdown_dir / f"{safe_name}.md"
            parent_chunks, child_chunks = self.rag_system.chunker.create_chunks_single(md_path)
            
            if not child_chunks:
                return False
                
            collection = self.rag_system.vector_db.get_collection(self.rag_system.collection_name)
            collection.add_documents(child_chunks)
            self.rag_system.parent_store.save_many(parent_chunks)
            return True
        except Exception as e:
            print(f"Error scraping and adding URL {url}: {e}")
            return False
    
    def get_markdown_files(self):
        if not self.markdown_dir.exists():
            return []
        return sorted([p.name[:-3] for p in self.markdown_dir.glob("*.md")])
        
    def remove_document(self, filename):
        md_name = filename + ".md"
        target = self.markdown_dir / md_name
        if target.exists():
            target.unlink()
            
        remaining = list(self.markdown_dir.glob("*.md"))
        
        self.rag_system.parent_store.clear_store()
        self.rag_system.vector_db.delete_collection(self.rag_system.collection_name)
        self.rag_system.vector_db.create_collection(self.rag_system.collection_name)
        
        added = 0
        if remaining:
            for md_path in remaining:
                try:
                    parent_chunks, child_chunks = self.rag_system.chunker.create_chunks_single(md_path)
                    if child_chunks:
                        collection = self.rag_system.vector_db.get_collection(self.rag_system.collection_name)
                        collection.add_documents(child_chunks)
                        self.rag_system.parent_store.save_many(parent_chunks)
                        added += 1
                except Exception as e:
                    print(f"Error rebuilding {md_path.name}: {e}")
        return added
    
    def clear_all(self):
        self.markdown_dir.mkdir(parents=True, exist_ok=True)
        clear_directory_contents(self.markdown_dir)
        
        self.rag_system.parent_store.clear_store()
        self.rag_system.vector_db.delete_collection(self.rag_system.collection_name)
        self.rag_system.vector_db.create_collection(self.rag_system.collection_name)
