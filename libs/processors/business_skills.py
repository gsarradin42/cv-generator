# import yaml
from libs.helpers.load_yaml import load_yaml
from libs.helpers.text_utils import gen_tag, gen_tag_nl, indent_line
from libs.services import i18n


def process(project) -> str:
    _ = i18n.get_translator()
    lang = i18n.get_lang()

    data = load_file(project)

    title = data.get("title_" + lang)

    table = gen_tag_nl(
        "table",
        "\n".join(
            [
                indent_line(
                    gen_tag(
                        "tr",
                        gen_tag("td", obj_lang.get(lang)[0])
                        + gen_tag("td", obj_lang.get(lang)[1]),
                    )
                )
                for _, obj_lang in data.get("list").items()
            ]
        ),
    )

    # return yaml.dump(data)

    return f"<h2>{title}</h2>\n{indent_line(table)}\n"


def load_file(project):
    return load_yaml(project, "business_skills.yml")
