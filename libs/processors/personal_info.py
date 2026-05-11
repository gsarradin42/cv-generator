from libs.helpers.load_yaml import load_yaml
from libs.helpers.text_utils import indent_multiple_line
from libs.models.adress import Adress

# from libs.processors.processor import Processor
from libs.services import i18n


def process(project: str):
    _ = i18n.get_translator()

    data = load_file(project)

    ad = data.get("adress")
    adress = Adress(
        ad.get("street_name"),
        ad.get("street_number"),
        ad.get("zip_code"),
        ad.get("city"),
        ad.get("country"),
    )

    title_data = i18n.get_data_keylang(data, "title")
    xp_data = f"{data.get('xp')} {_('years of experience')}"
    nationality_data = _("nationality").format(
        name=i18n.get_data_keylang(data, "nationality")
    )
    permit_data = _("work_permit_short").format(name=data.get("work_permit"))

    left_info = (
        f"<p class='title'>{title_data}</p>",
        f"<p class='xp'>{xp_data}</p>",
        f"<p class='nationality>{nationality_data} ({permit_data})</p>",
        f"<p class='adress'>{adress}</p>",
    )

    right_info = (
        f"<p class='name'>{data.get('first_name')} {data.get('last_name').upper()}</p>",
        f"<p class='tel'>{_('tel_short')} : {data.get('tel')}</p>",
        f"<p class='mail'>{_('mail_short')} : {data.get('mail')}</p>",
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
