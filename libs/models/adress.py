class Adress:
    def __init__(
        self,
        street_name=None,
        street_number=None,
        zip_code=None,
        city=None,
        country=None,
        adress=None,
    ):
        if adress is not None:
            print(f">> Adress > Adress is {adress.get('city')}")
            street_name = adress.get("street_name")
            street_number = adress.get("street_number")
            zip_code = adress.get("zip_code")
            city = adress.get("city")
            country = adress.get("country")

        self.street_name = street_name
        self.street_number = street_number
        self.zip_code = zip_code
        self.city = city
        self.country = country

    def __str__(self, zone=None, show_country=False):
        return "{:s} {:d} – {:d} {:s}".format(
            self.street_name, self.street_number, self.zip_code, self.city
        )
