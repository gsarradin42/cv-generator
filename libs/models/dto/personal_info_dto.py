class PersonalInfoDto:
    def __init__(
        self, title, fullname, tel, mail, adress, xp, nationality, work_permit
    ) -> None:
        self.title = title
        self.fullname = fullname
        self.tel = tel
        self.mail = mail
        self.adress = adress
        self.xp = xp
        self.nationality = nationality
        self.work_permit = work_permit
