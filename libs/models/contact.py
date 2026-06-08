from libs.models.adress import Adress


class Contact:
    def __init__(self, tel=None, mail=None, adress=None, data=None):
        if data is not None:
            tel = data.get("tel")
            mail = data.get("mail")
            adress = Adress(data=adress)

        self.tel = tel
        self.mail = mail
        self.adress = adress
