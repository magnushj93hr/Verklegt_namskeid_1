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
        return f"  {self.name:<20}{self.id:<11}{self.address:<20}{self.homeline:<11}{self.email:<30}{self.location:<20}{self.phone:<20}"