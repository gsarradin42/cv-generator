class Adress:
    def __init__(
        self,
        street_name=None,
        street_number=None,
        zip_code=None,
        city=None,
        country=None,
        data=None,
    ):
        if data is not None:
            print(f">> Adress > Adress is {data.get('city')}")
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

    def __str__(self, zone=None, show_country=False):
        return "{:s} {:d} – {:d} {:s}".format(
            self.street_name, self.street_number, self.zip_code, self.city
        )
