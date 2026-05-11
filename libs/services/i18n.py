import gettext
import locale
import os

from globals import BASE_DIR

# FIXME try to use project root here
LOCALES_DIR = os.path.join(BASE_DIR, "locales")
DOMAIN = "messages"
LANG_FALLBACK = "en"


def _detect_lang() -> str:
    lang, _ = locale.getdefaultlocale()
    if lang:
        return lang.split("_")[0]
    return LANG_FALLBACK


_current_translation = gettext.NullTranslations()
_current_lang = _detect_lang()
_ = None


def get_lang():
    return _current_lang


def get_translator(lang_code=None):
    # Si aucun code langue fourni, utiliser la locale système
    global _
    # if lang_code is None:
    #     lang_code, _x = locale.getdefaultlocale()
    #     if lang_code:
    #         lang_code = lang_code.split("_")[0]
    # Fallback à 'en' si introuvable
    # if not lang_code:
    #     lang_code = "en"
    try:
        trans = gettext.translation(
            DOMAIN, localedir=LOCALES_DIR, languages=[_current_lang]
        )
        trans.install()
        _ = trans.gettext
    except FileNotFoundError as e:
        print(f"Fichier introuvable: {e.filename} (errno={e.errno})")  # Utiliser gett
        # ext nul (retourne la chaîne originale)
        gettext.install(DOMAIN)
        _ = gettext.gettext
    return _


def set_language(lang_code: str | None = None):
    """
    Charge la traduction pour lang_code (ex: 'fr', 'en').
    Si lang_code est None, utilise la locale système.
    Retourne l'objet translation et le code utilisé.
    """
    global _current_translation
    global _current_lang
    if lang_code is None:
        lang_code = _detect_lang()
    try:
        trans = gettext.translation(
            DOMAIN, localedir=LOCALES_DIR, languages=[lang_code]
        )
    except FileNotFoundError:
        trans = gettext.NullTranslations()
    trans.install()  # installe _ et ngettext dans builtins
    _current_translation = trans
    _current_lang = lang_code
    return trans, lang_code


def get_translation() -> gettext.NullTranslations:
    """Retourne l'objet de traduction courant (pour appeler .gettext/.ngettext)."""
    return _current_translation


def get_data_keylang(data, key: str):
    value = data.get(f"{key}_{_current_lang}")
    return value if value else data.get(f"{key}_{LANG_FALLBACK}")
