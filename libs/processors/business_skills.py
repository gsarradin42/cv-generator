from libs.helpers.load_yaml import load_yaml
from libs.helpers.text_utils import (
    gen_tag,
    indent_line,
    indent_multiple_line,
)
from libs.services import i18n


def process(project) -> str:
    _ = i18n.get_translator()
    lang = i18n.get_lang()

    data = load_file(project)

    if data is None:
        return ""

    title = i18n.get_data_keylang(data, "title")

    table_lst = [
        indent_line(
            gen_tag(
                "tr",
                gen_tag("td", obj_lang.get(lang)[0])
                + gen_tag("td", obj_lang.get(lang)[1]),
            )
        )
        for _, obj_lang in data.get("list").items()
    ]

    # return yaml.dump(data)

    return f"""
    <section id="business-skills">
        <h2>{title}</h2>
        <table>
{indent_multiple_line(table_lst, 2)}
        </table>
    </section>
    """


def load_file(project):
    return load_yaml(project, "business_skills.yml")
