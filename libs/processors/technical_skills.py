from libs.helpers.load_yaml import load_yaml
from libs.helpers.text_utils import category_list_to_html_table_v2, indent_line
from libs.services import i18n


def process(project) -> str:
    _ = i18n.get_translator()
    lang = i18n.get_lang()

    data = load_file(project)

    title = data.get("title_" + lang)

    skill_list = data.get("list")

    table = category_list_to_html_table_v2(skill_list, "title_" + lang, "it_keywords")

    return f"<h2>{title}</h2>\n{indent_line(table)}\n"


def load_file(project):
    return load_yaml(project, "technical_skills.yml")
