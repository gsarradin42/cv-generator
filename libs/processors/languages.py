from libs.helpers.load_yaml import load_yaml
from libs.helpers.text_utils import gen_tag, indent_line, indent_multiple_line
from libs.services import i18n


def map(project: str):
    _ = i18n.get_translator()

    data = load_file(project).get("language")

    return {
        "title": _("languages"),
        "list": [
            (i18n.get_data_keylang(item, "title"), i18n.get_data_keylang(item, "level"))
            for item in data
        ],
    }


def process(project: str):
    _ = i18n.get_translator()

    data = load_file(project).get("language")

    table_lst = [
        indent_line(
            gen_tag(
                "tr",
                gen_tag("td", i18n.get_data_keylang(item, "title"))
                + gen_tag("td", i18n.get_data_keylang(item, "level")),
            )
        )
        for item in data
    ]

    return f"""
    <section id="languages">
        <h2>{_("languages")}</h2>
        <table>
{indent_multiple_line(table_lst, 2)}
        </table>
    </section>
    """


def load_file(project):
    return load_yaml(project, "formation.yml")
