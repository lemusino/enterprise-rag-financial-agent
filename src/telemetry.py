from langchain_core.callbacks import BaseCallbackHandler
from src.config import COSTO_PROMPT_PER_1M, COSTO_COMPLETION_PER_1M, TIPO_CAMBIO_MXN

class LLMOpsTelemetryHandler(BaseCallbackHandler):
    def __init__(self, session_state):
        self.session_state = session_state

    def on_llm_end(self, response, **kwargs):
        usage = {}
        try:
            gen = response.generations[0][0]
            if hasattr(gen, "message") and hasattr(gen.message, "usage_metadata"):
                usage = gen.message.usage_metadata or {}
        except Exception:
            pass

        t_in = usage.get("input_tokens", usage.get("prompt_token_count", 0))
        t_out = usage.get("output_tokens", usage.get("candidates_token_count", 0))
        total_tokens = usage.get("total_tokens", t_in + t_out)

        costo_usd = ((t_in / 1_000_000) * COSTO_PROMPT_PER_1M) + ((t_out / 1_000_000) * COSTO_COMPLETION_PER_1M)
        costo_mxn = costo_usd * TIPO_CAMBIO_MXN

        self.session_state.tokens_totales += total_tokens
        self.session_state.costo_acumulado_mxn += costo_mxn
