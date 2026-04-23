# css.py

STYLE_CSS = '''
    /* --- CONFIGURATION DE BASE --- */
    body {
        background-color: #f8fafc;
        font-family: sans-serif;
        margin: 0;
        padding: 0;
    }

    /* --- ANIMATION (Douce et rapide) --- */
    @keyframes entranceAnim {
        0% { transform: translateY(30px); opacity: 0; }
        100% { transform: translateY(0); opacity: 1; }
    }

    .animate-entrance {
        animation: entranceAnim 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards !important;
        background-color: #1e293b !important;
        color: white !important;
    }

    /* --- GRILLE & CARTES ACCUEIL (Compact pour Mobile) --- */
    .grid-container {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 10px;
        width: 100%;
        padding: 8px 12px;
    }

    .q-card {
        border: 2px solid #e2e8f0;
        cursor: pointer !important;
        border-radius: 20px !important;
        height: 100px !important; /* Gain de place mobile */
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 4px !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
        transition: transform 0.2s;
    }
    
    .q-card:active {
        transform: scale(0.95); /* Effet de clic sur mobile */
    }

    .q-card label {
        font-size: 11px !important;
        line-height: 1.1 !important;
    }

    .q-card i {
        font-size: 1.3rem !important;
        margin-bottom: 2px !important;
    }

    /* --- HEADER (Fixe et fin) --- */
    .sticky-header {
        position: sticky;
        top: 0;
        z-index: 1000;
        background-color: rgba(248, 250, 252, 0.95);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        border-bottom: 1px solid #e2e8f0;
        width: 100%;
        height: 44px;
        overflow: hidden; 
    }

    .header-row {
        display: flex !important;
        flex-wrap: nowrap !important;
        align-items: center !important;
        justify-content: space-between !important;
        width: 100%;
        height: 100%;
        padding: 0 12px !important;
    }

    /* --- STYLE DES ANNEXES (Correction Ordi + Mobile) --- */
    .annexe-content {
        display: flex;
        flex-direction: column;
        gap: 15px;
        width: 100%;
        max-width: 800px; /* Évite l'étalement sur PC */
        margin: 0 auto;
        padding: 10px;
    }

    .annexe-card {
        border-radius: 24px !important;
        border-top: 6px solid #1e3a8a !important; /* Barre bleue pro */
        padding: 1.5rem !important;
        height: auto !important; /* Important : laisse le texte respirer */
        background-color: white !important;
    }

    .special-label {
        font-size: 11px !important;
        font-weight: 900 !important;
        color: #1e293b !important;
    }
'''

# Boutons des listes
BTN_STYLE = "w-full h-auto py-3 bg-white text-black border-2 border-slate-200 rounded-xl px-4 text-center mb-2 font-medium shadow-sm uppercase text-sm"
