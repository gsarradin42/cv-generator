import markdown

from libs.helpers.load_yaml import load_yaml
from libs.services import i18n


def map(project: str):
    _ = i18n.get_translator()
    lang = i18n.get_lang()
    data = load_file(project)
    return {
        "content": markdown.markdown(data.get(lang)),
        "info": data.get("info").get(lang),
    }


def load_file(project):
    return load_yaml(project, "tagline.yml")
