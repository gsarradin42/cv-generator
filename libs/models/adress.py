class Adress:
    def __init__(self, street_name, street_number, zip_code, city, country=None):
        self.street_name = street_name
        self.street_number = street_number
        self.zip_code = zip_code
        self.city = city
        self.country = country

    def __str__(self, zone=None, show_country=False):
        return "{:s} {:d} – {:d} {:s}".format(
            self.street_name, self.street_number, self.zip_code, self.city
        )
