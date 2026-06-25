import markdown

from libs.models.xp import XP


class XpDto:
    def __init__(self, data: XP, dir: str) -> None:
        # self.start_date = data.start_date
        # self.end_date = data.end_date
        self.dir = dir
        self.business_domain = data.business_domain.capitalize()
        self.short_title = data.short_title
        self.title = data.title
        self.position = data.position
        self.location = data.location
        if data.tasks:
            self.tasks = markdown.markdown(data.tasks)
        if data.introduction:
            self.intro_or_summary = markdown.markdown(data.introduction)
        if not data.tasks and not data.introduction:
            self.intro_or_summary = markdown.markdown(data.summary)

        self.it_keywords = (", ".join(data.it_keywords), data.it_keywords)
        self.period = data.period_string
