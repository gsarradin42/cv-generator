from yaml import dump

from libs.helpers.load_yaml import load_yaml
from libs.helpers.text_utils import gen_tag, indent_line, indent_multiple_line
from libs.services import i18n


def process(project: str):
    _ = i18n.get_translator()

    data = load_file(project).get("formation")

    table_lst = [
        indent_line(
            gen_tag(
                "tr",
                gen_tag("td", item.get("organization"))
                + gen_tag(
                    "td",
                    f"{item.get('year')} – {i18n.get_data_keylang(item, 'content')}",
                ),
            )
        )
        for item in data
    ]

    return f"""
    <section id="formation">
        <h2>{_("formation")}</h2>
        <table>
{indent_multiple_line(table_lst, 2)}
        </table>
    </section>
    """


def load_file(project):
    return load_yaml(project, "formation.yml")
