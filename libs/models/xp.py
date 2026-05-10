from libs.helpers.date import date_to_mmyy, mmyy_to_date


class XP:
    def __init__(self, metadata, content):
        self.start_date = mmyy_to_date(metadata.get("period").get("start"))
        self.end_date = mmyy_to_date(metadata.get("period").get("end"))
        self.business_domain = metadata.get("business_domain")
        self.short_title = metadata.get("short_title")
        self.title = content.get("title")
        self.position = content.get("position")
        self.summary = content.get("summary")
        self.introduction = content.get("introduction")
        self.tasks = content.get("tasks")
        self.it_keywords = metadata.get("it_keywords")

    def get_period_string(self):
        start_dt = date_to_mmyy(self.start_date)
        if not self.end_date:
            return f"{_('since')} {start_dt}"

        end_dt = date_to_mmyy(self.end_date)
        return f"{start_dt} — {end_dt}"
