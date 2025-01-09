# utils/translation_manager.py
import json
import os

class TranslationManager:
    def __init__(self, language="en"):
        self.language = language
        self.translations = self._load_translations()

    def _load_translations(self):
        file_path = f"locales/{self.language}.json"
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        else:
            raise FileNotFoundError(f"Translation file for {self.language} not found.")

    def get(self, key, **kwargs):
        """Retrieve a translation string, optionally formatting it with kwargs."""
        translation = self.translations.get(key, key)  # Fallback to key if translation not found
        return translation.format(**kwargs) if kwargs else translation