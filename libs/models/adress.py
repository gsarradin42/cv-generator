class Adress:
    def __init__(
        self,
        street_name: str | None = None,
        street_number: str | None = None,
        zip_code: str | None = None,
        city: str | None = None,
        country: str | None = None,
        data=None,
    ):
        if data is not None:
            street_name = data.get("street_name")
            street_number = data.get("street_number")
            zip_code = data.get("zip_code")
            city = data.get("city")
            country = data.get("country")

        self.street_name = street_name
        self.street_number = street_number
        self.zip_code = zip_code
        self.city = city
        self.country = country

    def getAdressParts(self, zone: str, show_country=False):
        return (
            self.getAdressFirstPart(zone),
            f"{self.zip_code} {self.city}{' ' + self.country if self.country is not None and show_country else ''}",
        )

    def toString(self, zone: str, show_country=False):
        return " — ".join(self.getAdressParts(zone, show_country))

    def getAdressFirstPart(self, zone: str):
        match zone:
            case "BE" | "CH":
                return f"{self.street_name} {self.street_number}"
            case _:
                return f"{self.street_number} {self.street_name}"
