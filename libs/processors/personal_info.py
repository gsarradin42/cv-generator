from typing import cast

from libs.helpers.load_yaml import load_yaml
from libs.helpers.text_utils import indent_multiple_line
from libs.models.personal_info import PersonalInfo
from libs.services import i18n


def process(project="", pi: PersonalInfo | None = None):
    _ = i18n.get_translator()

    if project:
        data = load_file(project)
        pi = PersonalInfo(data=data)

    pi = cast(PersonalInfo, pi)

    xp_data = f"{pi.xp} {_('years of experience')}"
    nationality_data = _("nationality").format(name=pi.nationality)
    permit_data = _("work_permit_short").format(name=pi.work_permit)

    left_info = (
        f"<p class='title'>{pi.title}</p>",
        f"<p class='xp'>{xp_data}</p>",
        f"<p class='nationality'>{nationality_data} ({permit_data})</p>",
        f"<p class='adress'>{pi.adress}</p>",
    )

    right_info = (
        f"<p class='name'>{pi.first_name} {pi.last_name.upper()}</p>",
        f"<p class='tel'>{_('tel_short')} : {pi.tel}</p>",
        f"<p class='mail'>{_('mail_short')} : {pi.mail}</p>",
    )

    out = f"""<section id="personal-info">
        <div>
{indent_multiple_line(left_info, 3)}
        </div>
        <div>
{indent_multiple_line(right_info, 3)}
        </div>
    </section>
"""
    return out


def load_file(project):
    return load_yaml(project, "personal_info.yml")
