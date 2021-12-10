EMAIL = "@nanair.com"

class Employee:
    def __init__(self, name, id, address, homeline, location, phone, supervisor):
        self.name = name
        self.id = id
        self.address = address
        self.homeline = homeline
        self.location = location
        self.phone = phone
        self.supervisor = supervisor
        self.email = self.make_email()

    def make_email(self):
        """Creates an email for employee""" 
        first = str(self.name.split()[0]).lower()
        last = str(self.name.split()[-1]).lower()
        email = '{}.{}{}'.format(first, last, EMAIL)
        return email

    def __str__(self):
        return f"name: {self.name}, id: {self.id}, address: {self.address}, homeline: {self.homeline}, email: {self.email}, location: {self.location}, phone: {self.phone}, supervisor: {self.supervisor}"