class Employee:
    def __init__(self, name, id, address, homeline, email, location, phone):
        self.name = name
        self.id = id
        self.address = address
        self.homeline = homeline
        self.email = email
        self.location = location
        self.phone = phone

    def __str__(self):
        return f"name: {self.name}, id: {self.id}, address: {self.address}, phone {self.phone}, homeline {self.homeline}, email {self.email}, location {self.location}"