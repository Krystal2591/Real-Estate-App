class Purchase:
    def __init__(self, street, city, zipcode,
                 state, beds, baths, sq__ft,
                 home_type, sale_date, price,
                 latitude, longitude):
        self.longitude=longitude
        self.latitude=latitude
        self.price=price
        self.sale_date=sale_date
        self.type=home_type
        self.sq__ft=sq__ft
        self.baths=baths
        self.beds=beds
        self.state=state
        self.zip=zipcode
        self.city=city
        self.street=street

    @staticmethod
    def create_from_dict (dict):
        return Purchase(
                dict['street'],
                dict['city'],
                dict['zip'],
                dict['state'],
                int(dict['beds']),
                int(dict['baths']),
                int(dict['sq__ft']),
                dict['type'],
                dict['sale_date'],
                float(dict['price']),
                float(dict['latitude']),
                float(dict['longitude']))


