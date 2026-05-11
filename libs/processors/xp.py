import markdown

from libs.helpers.load_yaml import load_yaml
from libs.models.xp import XP
from libs.services import i18n


def process(xp_dir):
    _ = i18n.get_translator()

    xp_data = XP(**load(xp_dir))

    out = f"""<article>
    <header>
        <h2>{xp_data.title} / <span>{xp_data.business_domain}</span></h2>
        <h3>{xp_data.position}</h3>
        <span>{xp_data.get_period_string()}</span>
    </header>
    {markdown.markdown(xp_data.introduction)}
    <p>
        {markdown.markdown(xp_data.tasks)}
    </p>
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
