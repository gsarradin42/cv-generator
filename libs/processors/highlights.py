import os

from libs.helpers.load_yaml import load_yaml
from libs.models.xp import XP
from libs.processors import xp as xp_proc
from libs.services import i18n


def process(project: str):
    _ = i18n.get_translator()

    data = load_file(project)

    return f"""
    <section id="highlights">
    <h3>{_("highlights")}</h3>
    {"\n".join([get_xp_content(project, xp_item) for xp_item in data])}
    </section>
    """


def get_xp_content(project, xp_item):
    xp_dir = os.path.join(os.getcwd(), project, "XP", xp_item)
    xp = XP(**xp_proc.load(xp_dir))

    return f"<p><strong class='title'>{xp.short_title}</strong> <strong class='position'>{xp.position}</strong> {xp.summary}</p>"


def load_file(project):
    return load_yaml(project, "highlights.yml")
