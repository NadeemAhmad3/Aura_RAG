custom_css = """
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

    /* ============================================
       TYPOGRAPHY AND LOGO
       ============================================ */
    .app-header {
        display: flex;
        align-items: center;
        justify-width: space-between;
        width: 100%;
        margin-bottom: 20px;
    }
    
    .logo-container {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .logo-icon {
        font-size: 28px;
        color: #3b82f6;
        text-shadow: 0 0 15px rgba(59, 130, 246, 0.4);
    }

    .app-title {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
        font-size: 32px;
        font-weight: 800;
        letter-spacing: -0.5px;
        margin: 0 !important;
        padding: 0 !important;
        background: linear-gradient(90deg, #60a5fa, #3b82f6, #93c5fd);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-transform: uppercase;
    }

    /* ============================================
       MAIN CONTAINER
       ============================================ */
    .progress-text { 
        display: none !important;
    }
    
    .gradio-container { 
        max-width: 1300px !important;
        width: 100% !important;
        margin: 0 auto !important;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
        background: #0f0f0f !important;
    }

    /* ============================================
       CUSTOM UI ELEMENTS
       ============================================ */
    .toggle-btn { 
        margin-left: auto !important; 
        display: inline-flex !important; 
        align-items: center !important;
        justify-content: center !important;
        gap: 6px !important;
        padding: 4px 12px !important;
        background: linear-gradient(145deg, #1e293b, #0f172a) !important;
        color: #f8fafc !important;
        border: 1px solid #334155 !important;
        border-radius: 6px !important;
        box-shadow: 0 2px 4px -1px rgba(0, 0, 0, 0.5) !important;
        font-weight: 500 !important;
        font-size: 13px !important;
        transition: all 0.2s ease !important;
        width: auto !important;
        min-width: 0 !important;
        height: auto !important;
        line-height: normal !important;
    }
    .toggle-btn:hover {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 10px rgba(59, 130, 246, 0.3) !important;
        transform: translateY(-1px) !important;
    }
    .sidebar-col { 
        padding: 18px; 
        background: #151515; 
        border-radius: 12px; 
        border: 1px solid #262626; 
        box-shadow: inset 0 0 20px rgba(0,0,0,0.5);
        height: fit-content;
    }
    
    .doc-row {
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
        padding: 8px 12px !important;
        background: #1e1e1e !important;
        border: 1px solid #333 !important;
        border-radius: 8px !important;
        margin-bottom: 8px !important;
    }
    .doc-row > p {
        margin: 0 !important;
        color: #e2e8f0 !important;
        font-size: 14px !important;
        font-weight: 500 !important;
    }
    .delete-btn {
        background: transparent !important;
        border: none !important;
        color: #ef4444 !important;
        min-width: 24px !important;
        width: 24px !important;
        padding: 0 !important;
        height: 24px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        box-shadow: none !important;
    }
    .delete-btn:hover {
        background: rgba(239, 68, 68, 0.1) !important;
        transform: scale(1.1) !important;
    }

    .header-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
        margin-bottom: 5px;
    }
    .sidebar-header {
        font-size: 18px;
        font-weight: 600;
        color: #e2e8f0;
        margin-bottom: 5px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    /* ============================================
       TABS
       ============================================ */
    button[role="tab"] {
        color: #a3a3a3 !important;
        border-bottom: 2px solid transparent !important;
        border-radius: 0 !important;
        transition: all 0.2s ease !important;
        background: transparent !important;
    }
    
    button[role="tab"]:hover {
        color: #e5e5e5 !important;
    }
    
    button[role="tab"][aria-selected="true"] {
        color: #ffffff !important;
        border-bottom: 2px solid #ffffff !important;
        border-radius: 0 !important;
        background: transparent !important;
    }
    
    .tabs {
        border-bottom: none !important;
        border-radius: 0 !important;
    }
    
    .tab-nav {
        border-bottom: 1px solid #3f3f3f !important;
        border-radius: 0 !important;
    }
    
    button[role="tab"]::before,
    button[role="tab"]::after,
    .tabs::before,
    .tabs::after,
    .tab-nav::before,
    .tab-nav::after {
        display: none !important;
        content: none !important;
        border-radius: 0 !important;
    }
    
    #doc-management-tab {
        max-width: 500px !important;
        margin: 0 auto !important;
    }
    
    /* ============================================
       BUTTONS
       ============================================ */
    button {
        border-radius: 8px !important;
        border: none !important;
        font-weight: 500 !important;
        transition: all 0.2s ease !important;
        box-shadow: none !important;
    }
    
    .primary {
        background: #3b82f6 !important;
        color: white !important;
    }
    
    .primary:hover {
        background: #2563eb !important;
        transform: translateY(-1px) !important;
    }
    
    .stop {
        background: #ef4444 !important;
        color: white !important;
    }
    
    .stop:hover {
        background: #dc2626 !important;
        transform: translateY(-1px) !important;
    }
    
    /* ============================================
       CHAT INPUT BOX (#chat-input)
       ============================================ */
    #chat-input {
        background: #141416 !important;
        border: 1px solid #2d2d30 !important;
        border-radius: 14px !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.5) !important;
        padding: 6px 12px !important;
    }

    #chat-input:focus-within {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 1px #3b82f6, 0 0 15px rgba(59, 130, 246, 0.25) !important;
        background: #18181c !important;
    }

    #chat-input textarea {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        color: #f4f4f5 !important;
        font-size: 15px !important;
        padding: 8px 4px !important;
        outline: none !important;
        resize: none !important;
    }

    #chat-input textarea::placeholder {
        color: #71717a !important;
    }

    /* Prevent worst typing styling / background shift on autofill */
    #chat-input textarea:-webkit-autofill,
    #chat-input textarea:-webkit-autofill:hover, 
    #chat-input textarea:-webkit-autofill:focus {
        -webkit-text-fill-color: #f4f4f5 !important;
        -webkit-box-shadow: 0 0 0px 1000px #141416 inset !important;
        transition: background-color 5000s ease-in-out 0s !important;
    }

    /* Target the container/wrapper inside Gradio MultimodalTextbox to make it transparent */
    #chat-input > div,
    #chat-input .wrap {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        gap: 8px !important;
    }

    /* ============================================
       BUTTONS INSIDE CHAT INPUT BOX
       ============================================ */
    /* Target the upload arrow/button in MultimodalTextbox */
    #chat-input button.upload-button,
    #chat-input [data-testid="upload-button"],
    #chat-input button:has(svg) {
        background: rgba(59, 130, 246, 0.1) !important;
        border: 1px solid rgba(59, 130, 246, 0.2) !important;
        color: #3b82f6 !important;
        border-radius: 50% !important;
        width: 36px !important;
        height: 36px !important;
        min-width: 36px !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        cursor: pointer !important;
        transition: all 0.2s ease !important;
        padding: 0 !important;
    }

    #chat-input button.upload-button:hover,
    #chat-input [data-testid="upload-button"]:hover,
    #chat-input button:has(svg):hover {
        background: rgba(59, 130, 246, 0.2) !important;
        border-color: #3b82f6 !important;
        transform: scale(1.05) !important;
    }

    /* Style the upload arrow / SVG inside the button */
    #chat-input button.upload-button svg,
    #chat-input [data-testid="upload-button"] svg,
    #chat-input button:has(svg) svg {
        fill: #3b82f6 !important;
        stroke: #3b82f6 !important;
        width: 18px !important;
        height: 18px !important;
    }

    /* Target submit button in input textbox */
    #chat-input button.submit-button,
    #chat-input [data-testid="submit-button"] {
        background: linear-gradient(135deg, #3b82f6, #2563eb) !important;
        border: none !important;
        border-radius: 50% !important;
        width: 36px !important;
        height: 36px !important;
        min-width: 36px !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        cursor: pointer !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 4px 10px rgba(59, 130, 246, 0.3) !important;
        padding: 0 !important;
        margin-left: 4px !important;
    }

    #chat-input button.submit-button:hover,
    #chat-input [data-testid="submit-button"]:hover {
        background: linear-gradient(135deg, #60a5fa, #3b82f6) !important;
        transform: scale(1.05) !important;
        box-shadow: 0 6px 15px rgba(59, 130, 246, 0.4) !important;
    }

    #chat-input button.submit-button svg,
    #chat-input [data-testid="submit-button"] svg {
        fill: #ffffff !important;
        stroke: #ffffff !important;
        width: 16px !important;
        height: 16px !important;
    }

    /* File chips/preview in textbox */
    #chat-input .file-preview,
    #chat-input .file-parts,
    #chat-input .file-chip {
        background: #27272a !important;
        border: 1px solid #3f3f46 !important;
        border-radius: 8px !important;
        padding: 4px 8px !important;
        margin: 2px !important;
        color: #e4e4e7 !important;
        display: inline-flex !important;
        align-items: center !important;
        gap: 6px !important;
        font-size: 13px !important;
    }

    /* ============================================
       CHAT WINDOW (#chat-window)
       ============================================ */
    #chat-window {
        background: #09090b !important;
        border: 1px solid #202024 !important;
        border-radius: 16px !important;
        box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.7) !important;
        padding: 16px !important;
        overflow-y: auto !important;
    }

    /* Scrollbar */
    #chat-window::-webkit-scrollbar,
    #chat-window .message-wrap::-webkit-scrollbar {
        width: 6px !important;
    }
    #chat-window::-webkit-scrollbar-track,
    #chat-window .message-wrap::-webkit-scrollbar-track {
        background: transparent !important;
    }
    #chat-window::-webkit-scrollbar-thumb,
    #chat-window .message-wrap::-webkit-scrollbar-thumb {
        background: #27272a !important;
        border-radius: 10px !important;
    }
    #chat-window::-webkit-scrollbar-thumb:hover,
    #chat-window .message-wrap::-webkit-scrollbar-thumb:hover {
        background: #3b82f6 !important;
    }

    /* Message Bubbles layout */
    .message-row {
        margin-bottom: 20px !important;
    }

    /* User Bubble */
    #chat-window .message.user,
    .chatbot .message.user {
        background: linear-gradient(135deg, #1e40af, #3b82f6) !important;
        color: #ffffff !important;
        border-radius: 16px 16px 2px 16px !important;
        padding: 14px 18px !important;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.2) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        font-size: 15px !important;
        line-height: 1.6 !important;
        max-width: 80% !important;
        align-self: flex-end !important;
    }

    /* Bot Bubble */
    #chat-window .message.bot,
    .chatbot .message.bot {
        background: #18181b !important;
        color: #e4e4e7 !important;
        border-radius: 16px 16px 16px 2px !important;
        padding: 16px 20px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3) !important;
        border: 1px solid #27272a !important;
        border-left: 3px solid #3b82f6 !important;
        font-size: 15px !important;
        line-height: 1.6 !important;
        max-width: 85% !important;
    }

    /* Chat bubble Links */
    #chat-window a,
    .chatbot a,
    .message a {
        color: #60a5fa !important;
        text-decoration: none !important;
        font-weight: 600 !important;
        background: rgba(59, 130, 246, 0.1) !important;
        padding: 3px 8px !important;
        border-radius: 6px !important;
        border: 1px solid rgba(59, 130, 246, 0.2) !important;
        display: inline-flex !important;
        align-items: center !important;
        gap: 6px !important;
        transition: all 0.2s ease !important;
    }

    #chat-window a:hover,
    .chatbot a:hover,
    .message a:hover {
        background: rgba(59, 130, 246, 0.2) !important;
        border-color: #3b82f6 !important;
        box-shadow: 0 0 8px rgba(59, 130, 246, 0.2) !important;
    }

    /* ============================================
       LANGGRAPH DETAILS / ACCORDION BLOCKS
       ============================================ */
    .chatbot details,
    #chat-window details,
    details.meta-wrap {
        background: #18181b !important;
        border: 1px solid #27272a !important;
        border-radius: 10px !important;
        margin: 10px 0 !important;
        padding: 0 !important;
        overflow: hidden !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
    }

    .chatbot details[open],
    #chat-window details[open],
    details.meta-wrap[open] {
        border-color: #3b82f6 !important;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.1) !important;
    }

    .chatbot summary,
    #chat-window summary,
    summary.meta-title {
        padding: 12px 16px !important;
        font-weight: 600 !important;
        color: #60a5fa !important;
        background: #202024 !important;
        cursor: pointer !important;
        user-select: none !important;
        display: flex !important;
        align-items: center !important;
        gap: 8px !important;
        transition: background 0.2s ease !important;
        outline: none !important;
        border-bottom: 1px solid transparent !important;
    }

    .chatbot details[open] summary,
    #chat-window details[open] summary,
    details.meta-wrap[open] summary {
        background: #1f1f23 !important;
        border-bottom: 1px solid #27272a !important;
    }

    .chatbot summary:hover,
    #chat-window summary:hover,
    summary.meta-title:hover {
        background: #27272a !important;
        color: #93c5fd !important;
    }

    /* Style inner text area of details */
    .chatbot details > div,
    #chat-window details > div,
    .chatbot .meta-content {
        padding: 14px 18px !important;
        background: #121214 !important;
        color: #d4d4d8 !important;
        font-size: 14px !important;
        line-height: 1.6 !important;
    }

    /* Code blocks inside details */
    .chatbot details pre,
    #chat-window details pre {
        background: #09090b !important;
        border: 1px solid #27272a !important;
        border-radius: 6px !important;
        padding: 10px !important;
        margin: 6px 0 0 0 !important;
    }

    /* ============================================
       INPUTS & TEXTAREAS (GENERAL)
       ============================================ */
    input, 
    textarea {
        background: #18181b !important;
        border: 1px solid #27272a !important;
        border-radius: 8px !important;
        color: #e4e4e7 !important;
        transition: border-color 0.2s ease !important;
    }
    
    input:focus, 
    textarea:focus {
        border-color: #3b82f6 !important;
        outline: none !important;
        box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.2) !important;
    }
    
    textarea[readonly] {
        background: #18181b !important;
        color: #a1a1aa !important;
    }

    /* ============================================
       FILE UPLOAD GENERAL DOCK
       ============================================ */
    .file-preview, 
    [data-testid="file-upload"] {
        background: #121214 !important;
        border: 1px dashed #27272a !important;
        border-radius: 10px !important;
        color: #e4e4e7 !important;
        min-height: 180px !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        align-items: center !important;
        transition: all 0.2s ease !important;
    }
    
    .file-preview:hover, 
    [data-testid="file-upload"]:hover {
        border-color: #3b82f6 !important;
        background: #18181b !important;
    }

    /* ============================================
       FILE LIST BOX
       ============================================ */
    #file-list-box {
        background: #18181b !important;
        border: 1px solid #27272a !important;
        border-radius: 10px !important;
        padding: 12px !important;
    }
    
    #file-list-box textarea {
        background: transparent !important;
        border: none !important;
        color: #e4e4e7 !important;
        padding: 0 !important;
    }

    /* ============================================
       PROGRESS BAR
       ============================================ */
    .progress-bar-wrap {
        border-radius: 8px !important;
        overflow: hidden !important;
        background: #27272a !important;
    }

    .progress-bar {
        border-radius: 8px !important;
        background: linear-gradient(90deg, #3b82f6, #60a5fa) !important;
    }
    
    /* ============================================
       TYPOGRAPHY
       ============================================ */
    h1, h2, h3, h4, h5, h6 {
        color: #f4f4f5 !important;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif !important;
    }

    /* ============================================
       GLOBAL OVERRIDES
       ============================================ */
    * {
        box-shadow: none !important;
    }
    
    footer {
        visibility: hidden !important;
        display: none !important;
    }

    /* ============================================
       AUTH / LOGIN PANEL
       ============================================ */
    .auth-logo-wrapper {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        margin-bottom: 24px !important;
        width: 100% !important;
    }
    .auth-logo-wrapper .logo-container {
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 12px !important;
    }

    .auth-container {
        max-width: 440px !important;
        margin: 120px auto !important;
        background: #141416 !important;
        border: 1px solid #2d2d30 !important;
        border-radius: 16px !important;
        padding: 40px !important;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.6) !important;
        transition: all 0.3s ease !important;
    }
    .auth-container:hover {
        border-color: #3b82f6 !important;
        box-shadow: 0 12px 48px rgba(0, 0, 0, 0.7), 0 0 30px rgba(59, 130, 246, 0.1) !important;
    }

    .auth-subtitle {
        text-align: center !important;
        color: #71717a !important;
        margin-bottom: 30px !important;
        font-size: 14px !important;
        font-weight: 400 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    /* Premium segmented control for Radio buttons (Login/Signup toggle) */
    .auth-container .gradio-radio {
        background: #0f0f0f !important;
        border: 1px solid #2d2d30 !important;
        border-radius: 8px !important;
        padding: 4px !important;
        display: flex !important;
        justify-content: space-between !important;
        gap: 4px !important;
        margin-bottom: 20px !important;
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.3) !important;
    }
    .auth-container .gradio-radio label {
        flex: 1 !important;
        text-align: center !important;
        padding: 8px 12px !important;
        border-radius: 6px !important;
        font-weight: 600 !important;
        font-size: 14px !important;
        color: #71717a !important;
        cursor: pointer !important;
        transition: all 0.2s ease !important;
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        display: inline-flex !important;
        justify-content: center !important;
        align-items: center !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    .auth-container .gradio-radio label.selected {
        background: #27272a !important;
        color: #ffffff !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
    }
    .auth-container .gradio-radio input[type="radio"] {
        display: none !important;
    }

    /* Premium styled Textbox inputs */
    .auth-container .gradio-textbox {
        background: transparent !important;
        border: none !important;
        margin-bottom: 16px !important;
    }
    .auth-container .gradio-textbox input {
        background: #0f0f0f !important;
        border: 1px solid #2d2d30 !important;
        border-radius: 8px !important;
        padding: 12px 14px !important;
        font-size: 15px !important;
        color: #ffffff !important;
        transition: all 0.2s ease !important;
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.5) !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    .auth-container .gradio-textbox input:focus {
        border-color: #3b82f6 !important;
        background: #0f0f0f !important;
        box-shadow: 
            0 0 0 1px #3b82f6, 
            0 0 10px rgba(59, 130, 246, 0.2),
            inset 0 2px 4px rgba(0, 0, 0, 0.5) !important;
    }
    .auth-container .gradio-textbox input::placeholder {
        color: #71717a !important;
    }

    /* Submit Button */
    .auth-container button {
        background: #3b82f6 !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 12px 20px !important;
        font-size: 15px !important;
        font-weight: 600 !important;
        color: #ffffff !important;
        cursor: pointer !important;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3) !important;
        transition: all 0.2s ease !important;
        margin-top: 10px !important;
        width: 100% !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    .auth-container button:hover {
        background: #2563eb !important;
        box-shadow: 0 6px 16px rgba(59, 130, 246, 0.4) !important;
        transform: translateY(-1px) !important;
    }
    .auth-container button:active {
        transform: translateY(0) !important;
    }

    /* App layout general styling updates to match Plus Jakarta Sans */
    .gradio-container { 
        font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
    }
    h1, h2, h3, h4, h5, h6, .app-title {
        font-family: 'Outfit', -apple-system, sans-serif !important;
    }

    /* Logout / user info styling */
    .logout-btn {
        background: rgba(239, 68, 68, 0.08) !important;
        border: 1px solid rgba(239, 68, 68, 0.2) !important;
        color: #ef4444 !important;
        font-weight: 600 !important;
        transition: all 0.2s ease !important;
        width: auto !important;
        padding: 5px 14px !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    .logout-btn:hover {
        background: #ef4444 !important;
        color: #ffffff !important;
        box-shadow: 0 4px 12px rgba(239, 68, 68, 0.2) !important;
    }
    .user-info-text {
        color: #a1a1aa !important;
        font-size: 13px !important;
        font-weight: 500 !important;
        display: flex !important;
        align-items: center !important;
        margin-right: 12px !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    .header-right {
        display: flex !important;
        justify-content: flex-end !important;
        align-items: center !important;
        gap: 12px !important;
        margin-left: auto !important;
    }
"""
