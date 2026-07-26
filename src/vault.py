import re

class PrivacyVault:
    def __init__(self):
        self.patron_tarjeta = r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b'
        self.patron_rfc = r'\b[A-Z&Ñ]{3,4}\d{6}[A-V1-9][A-Z1-9][0-9A]\b'
        self.patron_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    def mask(self, text: str) -> tuple[str, dict]:
        vault = {}
        masked_text = text

        for i, t in enumerate(re.findall(self.patron_tarjeta, masked_text)):
            tag = f"[TARJETA_{i+1}]"
            vault[tag] = t
            masked_text = masked_text.replace(t, tag)

        for i, r in enumerate(re.findall(self.patron_rfc, masked_text)):
            tag = f"[RFC_{i+1}]"
            vault[tag] = r
            masked_text = masked_text.replace(r, tag)

        for i, e in enumerate(re.findall(self.patron_email, masked_text)):
            tag = f"[CORREO_{i+1}]"
            vault[tag] = e
            masked_text = masked_text.replace(e, tag)

        return masked_text, vault

    def unmask(self, masked_text: str, vault: dict) -> str:
        restored = str(masked_text)
        for tag, original in vault.items():
            restored = restored.replace(tag, original)
        return restored
