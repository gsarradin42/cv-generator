import gettext
import locale
import os

from globals import BASE_DIR

# FIXME try to use project root here
LOCALES_DIR = os.path.join(BASE_DIR, "locales")
DOMAIN = "messages"
LOCALE_FALLBACK = ("en", "US")


def _detect_locale() -> tuple[str, str]:
    locale_def, _ = locale.getdefaultlocale()
    if locale_def:
        lang_zone = locale_def.split(".")[0].split("_")
        return (lang_zone[0], lang_zone[1])
    return LOCALE_FALLBACK


_current_translation = gettext.NullTranslations()
(_current_lang, _current_zone) = _detect_locale()
_ = None


def get_lang():
    return _current_lang


def get_zone():
    return _current_zone


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
        lang_code = _detect_locale()[0]
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


def set_zone(zone_code: str | None = None):
    global _current_zone
    if zone_code is None:
        zone_code = _detect_locale()[1]
    _current_zone = zone_code


def get_translation() -> gettext.NullTranslations:
    """Retourne l'objet de traduction courant (pour appeler .gettext/.ngettext)."""
    return _current_translation


def get_data_keylang(data, key: str) -> str:
    value: str = data.get(f"{key}_{_current_lang}")
    if not value:
        value = data.get(key)
    if not value:
        value = data.get(f"{key}_{LOCALE_FALLBACK[0]}")

    return value
