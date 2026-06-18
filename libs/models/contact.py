from libs.models.adress import Adress


class Contact:
    def __init__(self, tel=None, mail=None, adress=None, data=None):
        if data is not None:
            tel = data.get("tel")
            mail = data.get("mail")
            if data.get("adress") is not None:
                adress = Adress(data=data.get("adress"))

        self.tel = tel
        self.mail = mail
        self.adress = adress
