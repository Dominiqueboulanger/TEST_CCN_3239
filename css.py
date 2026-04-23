# css.py

STYLE_CSS = '''
    /* --- CONFIGURATION DE BASE --- */
    body {
        background-color: #f8fafc;
        font-family: sans-serif;
        margin: 0;
        padding: 0;
    }

    /* --- ANIMATION (Optimisée) --- */
    @keyframes entranceAnim {
        0% { transform: translateY(50px); opacity: 0; }
        100% { transform: translateY(0); opacity: 1; }
    }

    .animate-entrance {
        animation: entranceAnim 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards !important;
        background-color: #1e293b !important;
        color: white !important;
    }

    /* --- GRILLE (Gain de place ici) --- */
    .grid-container {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 10px; /* On passe de 16px à 10px */
        width: 100%;
        padding: 8px 12px; /* On réduit le padding haut/bas */
    }

    /* --- CARTES MÉTIERS (Le secret est ici) --- */
    .q-card {
        border: 2px solid #e2e8f0;
        cursor: pointer !important;
        border-radius: 20px !important;
        height: 100px !important; /* On passe de 140px à 100px pour gagner 120px au total */
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 4px !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
    }

    /* Réduction de la taille du texte dans les cartes pour que ça reste harmonieux */
    .q-card label {
        font-size: 11px !important;
        line-height: 1.1 !important;
    }

    .q-card i {
        font-size: 1.3rem !important; /* Icônes légèrement plus petites */
        margin-bottom: 2px !important;
    }

    /* --- FIX DU HEADER (Très serré) --- */
    .sticky-header {
        position: sticky;
        top: 0;
        z-index: 1000;
        background-color: rgba(248, 250, 252, 0.95);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        border-bottom: 1px solid #e2e8f0;
        width: 100%;
        height: 44px; /* On passe de 50px à 44px (standard iOS) */
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
'''

# On allège aussi un peu les boutons des étapes suivantes
BTN_STYLE = "w-full h-auto py-3 bg-white text-black border-2 border-slate-200 rounded-xl px-4 text-center mb-2 font-medium shadow-sm uppercase text-sm"
