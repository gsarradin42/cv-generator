from libs.models.adress import Adress
from libs.services import i18n


class PersonalInfo:
    def __init__(
        self,
        first_name="",
        last_name="",
        tel="",
        mail="",
        title="",
        xp="",
        nationality="",
        work_permit="",
        adress=None,
        data=None,
    ):
        if data is not None:
            first_name = data.get("first_name")
            last_name = data.get("last_name")
            tel = data.get("tel")
            mail = data.get("mail")
            title = i18n.get_data_keylang(data, "title")
            xp = data.get("xp")
            nationality = i18n.get_data_keylang(data, "nationality")
            work_permit = data.get("work_permit")
            adress = data.get("adress")

        self.first_name = first_name
        self.last_name = last_name
        self.tel = tel
        self.mail = mail
        self.title = title
        self.xp = xp
        self.nationality = nationality
        self.work_permit = work_permit
        self.adress = Adress(adress=adress)
