# css.py

STYLE_CSS = '''
    /* --- CONFIGURATION GÉNÉRALE --- */
    body { background-color: #f8fafc; font-family: sans-serif; margin: 0; padding: 0; }

    /* --- ACCUEIL COMPACT (Mobile) --- */
    .grid-container {
        display: grid; grid-template-columns: repeat(2, 1fr);
        gap: 10px; width: 100%; padding: 8px 12px;
    }
    .q-card {
        border: 2px solid #e2e8f0; border-radius: 20px !important;
        height: 100px !important; display: flex; flex-direction: column;
        justify-content: center; padding: 4px !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
    }
    .q-card label { font-size: 11px !important; line-height: 1.1 !important; }
    .q-card i { font-size: 1.3rem !important; margin-bottom: 2px !important; }

    /* --- HEADER --- */
    .sticky-header {
        position: sticky; top: 0; z-index: 1000;
        background-color: rgba(248, 250, 252, 0.95);
        backdrop-filter: blur(8px); border-bottom: 1px solid #e2e8f0;
        width: 100%; height: 44px; overflow: hidden; 
    }
    .header-row {
        display: flex !important; align-items: center !important;
        justify-content: space-between !important; width: 100%; height: 100%;
        padding: 0 12px !important;
    }

    /* --- NETTOYAGE DES ANNEXES (Le correctif pour tes captures) --- */
    .annexe-container {
        display: flex; flex-direction: column; width: 100%;
        max-width: 700px; margin: 0 auto; padding: 20px; gap: 20px;
    }
    .annexe-title-section {
        display: flex; flex-direction: column; gap: 4px;
        margin-bottom: 10px; text-align: center;
    }
    .annexe-card-info {
        background: white; border-radius: 24px; padding: 25px;
        border: 2px solid #e2e8f0; border-top: 6px solid #1e3a8a;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    /* Empêche les icônes de flotter n'importe où */
    .annexe-card-info i, .annexe-card-info span { position: relative; }
'''

BTN_STYLE = "w-full h-auto py-3 bg-white text-black border-2 border-slate-200 rounded-xl px-4 text-center mb-2 font-medium shadow-sm uppercase text-sm"
