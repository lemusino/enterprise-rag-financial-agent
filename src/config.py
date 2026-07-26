import os

COSTO_PROMPT_PER_1M = 0.075
COSTO_COMPLETION_PER_1M = 0.30
TIPO_CAMBIO_MXN = float(os.getenv("TIPO_CAMBIO_MXN", 18.00))

CUSTOM_CSS = """
<style>
    .stApp {
        background-color: #F8F9FA;
    }
    section[data-testid="stSidebar"] {
        background-color: #1A202C !important;
        color: #FFFFFF !important;
    }
    h1, h2, h3 {
        color: #2D3748;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stButton>button {
        background-color: #EB0029 !important;
        color: white !important;
        border-radius: 6px;
        font-weight: bold;
    }
</style>
"""
