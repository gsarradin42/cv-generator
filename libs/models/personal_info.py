from libs.models.contact import Contact
from libs.services import i18n


class PersonalInfo:
    def __init__(
        self,
        first_name="",
        last_name="",
        title="",
        xp="",
        nationality="",
        work_permit="",
        contact=None,
        data=None,
    ):
        if data is not None:
            first_name = data.get("first_name")
            last_name = data.get("last_name")
            title = i18n.get_data_keylang(data, "title")
            xp = data.get("xp")
            nationality = data.get("nationality")
            work_permit = data.get("work_permit")
            contact = data.get("contact")

        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.xp = xp
        self.nationality = nationality
        self.work_permit = work_permit
        self.contact = Contact(data=contact)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
