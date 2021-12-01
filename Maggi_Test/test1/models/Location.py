class Location:
    def __init__(self, country,airport,phone,opening_hours):
        self.country = country
        self.airport = airport
        self.phone = phone
        self.opening_hours = opening_hours
        

    def __str__(self):
        return f"country: {self.country}, aiport: {self.airport}, phone: {self.phone}, opening hours: {self.opening_hours}"