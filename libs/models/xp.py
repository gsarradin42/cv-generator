from libs.helpers.date import date_to_mmyy, mmyy_to_date
from libs.services import i18n


class XP:
    def __init__(self, metadata, content):
        self.start_date = mmyy_to_date(metadata.get("period").get("start"))
        self.end_date = mmyy_to_date(metadata.get("period").get("end"))
        self.business_domain = content.get("business_domain")
        self._short_title = metadata.get("short_title")
        self.title = (
            content.get("title") if content.get("title") else metadata.get("title")
        )
        self.location = i18n.get_data_keylang(metadata, "location")
        self.position = (
            content.get("position")
            if content.get("position")
            else metadata.get("position")
        )
        self.summary = content.get("summary")
        self.introduction = content.get("introduction")
        self.tasks = content.get("tasks")
        self.it_keywords = metadata.get("it_keywords")

    @property
    def period_string(self):
        start_dt = date_to_mmyy(self.start_date)
        if not self.end_date:
            return f"{_('since')} {start_dt}"

        end_dt = date_to_mmyy(self.end_date)
        return f"{start_dt} – {end_dt}"

    @property
    def short_title(self):
        return self._short_title if self._short_title else self.title
