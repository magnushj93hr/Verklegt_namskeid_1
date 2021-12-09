class Location:
    def __init__(self, country, location,airport,phone,opening_hours):
        self.country = country
        self.location = location
        self.airport = airport
        self.phone = phone
        self.opening_hours = opening_hours

    def __str__(self):
        return f"country: {self.country}, location: {self.location}, aiport: {self.airport}, phone: {self.phone}, opening hours: {self.opening_hours}"