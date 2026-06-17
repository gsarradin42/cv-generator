import os

import markdown

from libs.helpers.load_yaml import load_yaml
from libs.models.dto.xp_dto import XpDto
from libs.models.xp import XP
from libs.services import i18n


def map(name):
    _ = i18n.get_translator()

    xp_dir_base = os.path.join(os.getcwd(), name, "XP")

    print("process XPs")

    listdir = filter(
        lambda f: os.path.isdir(os.path.join(xp_dir_base, f)), os.listdir(xp_dir_base)
    )

    return {
        "title": _("xp_pro"),
        "list": [_map_single(xp_dir_base, d) for d in sorted(listdir, reverse=True)],
    }


def _map_single(xp_dir_base, xp_dir):
    print(f"> process {xp_dir}")
    xp_data = XP(**load(os.path.join(xp_dir_base, xp_dir)))
    return XpDto(xp_data, dir=xp_dir)


def _process_single2(xp_dir_base, xp_dir):
    print(f">> Process {xp_dir}")
    _ = i18n.get_translator()

    xp_data = XP(**load(os.path.join(xp_dir_base, xp_dir)))

    out = f"""<article id="xp-{xp_dir}">
    <header>
        <h3><span class="main">{xp_data.title}</span> / <span class="business">{xp_data.business_domain.capitalize()}</span></h3>
        <h4 class="position">{xp_data.position}<span class="period">{xp_data.period_string}</span></h4>
    </header>
    <section class="introduction">
        {markdown.markdown(xp_data.introduction)}
    </section>
    <section class="tasks">
        {markdown.markdown(xp_data.tasks)}
    </section>
    <p class="it-keywords">
        {", ".join(xp_data.it_keywords)}
    </p>
</article>
"""
    return out


def load(xp_dir):
    return {
        "content": load_yaml(xp_dir, "content_" + i18n.get_lang() + ".yml"),
        "metadata": load_yaml(xp_dir, "metadata.yml"),
    }
