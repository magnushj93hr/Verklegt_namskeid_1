class Employee:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"name: {self.name}, email: {self.email}, phone: {self.phone}"