EMAIL = "@nanair.com"

class Employee:
    def __init__(self, name, id, address, homeline, location, phone):
        self.name = name
        self.id = id
        self.address = address
        self.homeline = homeline
        self.location = location
        self.phone = phone
        self.email = self.make_email()

    def make_email(self): 
        first = str(self.name.split()[0]).lower()
        last = str(self.name.split()[-1]).lower()
        email = '{}.{}{}'.format(first, last, EMAIL)
        return email

    def __str__(self):
        return f"name: {self.name}, id: {self.id}, address: {self.address}, homeline: {self.homeline}, email: {self.email}, location: {self.location}, phone: {self.phone}"