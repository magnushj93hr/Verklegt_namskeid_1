class Contractor:
    def __init__(self, name, contact, phone, opening_hours, location):
        self.name = name
        self.contact = contact
        self.phone = phone
        self.opening_hours = opening_hours
        self.location = location

    def __str__(self):
        return f"name: {self.name}, contact: {self.contact}, phone: {self.phone}, opening hours: {self.opening_hours}, location: {self.location}"