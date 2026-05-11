from libs.helpers.load_yaml import load_yaml
from libs.helpers.text_utils import category_list_to_html_table_v2, indent_multiple_line
from libs.services import i18n


def process(project) -> str:
    _ = i18n.get_translator()

    data = load_file(project)

    title = i18n.get_data_keylang(data, "title")

    skill_list = data.get("list")

    table = category_list_to_html_table_v2(skill_list, "title", "it_keywords")

    return f"""
    <section id="technical-skills">
        <h2>{title}</h2>
{indent_multiple_line(table, 2)}
    </section>
"""


def load_file(project):
    return load_yaml(project, "technical_skills.yml")
