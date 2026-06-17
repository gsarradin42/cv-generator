import markdown

from libs.helpers.load_yaml import load_yaml
from libs.services import i18n


def map(project: str):
    _ = i18n.get_translator()

    data = load_file(project)

    return {
        "title": _("interests"),
        "content": markdown.markdown(i18n.get_data_keylang(data, "content")),
    }


def process(project: str):
    _ = i18n.get_translator()

    data = load_file(project)

    return f"""
    <section id="interests">
        <h2>{_("interests")}</h2>
        {markdown.markdown(i18n.get_data_keylang(data, "content"))}
    </section>
    """


def load_file(project):
    return load_yaml(project, "interests.yml")
