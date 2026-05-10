from libs.helpers.load_yaml import load_yaml
from libs.services import i18n


def process(project: str):
    _ = i18n.get_translator()
    lang = i18n.get_lang()
    data = load_file(project)
    return f"""<aside class="tagline">
        <article>{data.get(lang)}</article>
        <p>{data.get("info").get(lang)}</p>
    </aside>
"""


def load_file(project):
    return load_yaml(project, "tagline.yml")
