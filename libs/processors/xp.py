import os

import markdown

from libs.helpers.load_yaml import load_yaml
from libs.helpers.text_utils import indent_multiple_line
from libs.models.personal_info import PersonalInfo
from libs.models.xp import XP
from libs.services import i18n


def process(name, data: PersonalInfo):
    _ = i18n.get_translator()

    xp_dir_base = os.path.join(os.getcwd(), name, "XP")

    print("process XPs")

    listdir = filter(
        lambda f: os.path.isdir(os.path.join(xp_dir_base, f)), os.listdir(xp_dir_base)
    )

    return f"""
    <section id="xp">
        <span class="set-heading left">{data.title}</span>
        <span class="set-heading right">{data.first_name} {data.last_name}</span>
        <h2>{_("xp_pro")}</h2>
    {indent_multiple_line("\n".join([_process_single(xp_dir_base, d) for d in sorted(listdir, reverse=True)]), 2)}
    </section>
    """


def _process_single(xp_dir_base, xp_dir):
    print(f">> Process {xp_dir}")
    _ = i18n.get_translator()

    xp_data = XP(**load(os.path.join(xp_dir_base, xp_dir)))

    out = f"""<article id="xp-{xp_dir}">
    <header>
        <h3><span class="main">{xp_data.title}</span> / <span class="business">{xp_data.business_domain}</span></h3>
        <h4 class="position">{xp_data.position}<span class="period">{xp_data.get_period_string()}</span></h4>
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
