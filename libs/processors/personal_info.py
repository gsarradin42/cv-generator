from typing import cast

from libs.helpers.load_yaml import load_yaml
from libs.models.dto.personal_info_dto import PersonalInfoDto
from libs.models.personal_info import PersonalInfo
from libs.services import i18n


def map(project="", pi: PersonalInfo | None = None) -> PersonalInfoDto:
    _ = i18n.get_translator()

    if project:
        data = load_file(project)
        pi = PersonalInfo(data=data)

    pi = cast(PersonalInfo, pi)

    xp_data = f"{pi.xp} {_('years of experience')}"
    nationality_data = _("nationality").format(name=pi.nationality)
    permit_data = None
    if i18n.get_zone() != "FR":
        permit_data = _("work_permit_short").format(name=pi.work_permit)

    return PersonalInfoDto(
        pi.title,
        f"{pi.first_name} {pi.last_name.upper()}",
        (_("tel_short"), pi.contact.tel),
        (_("mail_short"), pi.contact.mail),
        pi.contact.adress.getAdressParts(i18n.get_zone())
        if pi.contact.adress is not None
        else None,
        xp_data,
        nationality_data,
        permit_data,
    )


def load_file(project):
    return load_yaml(project, "personal_info.yml")
