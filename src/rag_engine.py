from langchain_google_genai import ChatGoogleGenerativeAI

BASE_CONOCIMIENTO_CNBV = """
[CIRCULAR ÚNICA DE BANCOS - ARTÍCULO 11]
Las Instituciones de Banca Múltiple deberán mantener un Coeficiente de Capital Fundamental (CCF)
mínimo del 4.5% respecto a los Activos Ponderados por Riesgo (APR). Adicionalmente, se requerirá un
suplemento de conservación de capital del 2.5%, sumando un total exigido del 7.0%.
El incumplimiento de este umbral detonará Medidas Correctivas Mínimas inmediatas por la CNBV.
"""

def invocar_agente_rag(prompt_usuario: str, api_key: str, callbacks: list) -> str:
    llm = ChatGoogleGenerativeAI(
        model="gemini-flash-latest",
        google_api_key=api_key,
        temperature=0,
        callbacks=callbacks
    )

    system_prompt = f"""Eres un oficial de cumplimiento normativo bancario.
