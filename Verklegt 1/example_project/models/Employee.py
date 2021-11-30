class Employee:
    def __init__(self, name, emp_id, address, homeline, email, phone, location):
        self.name = name
        self.emp_id = emp_id
        self.address = address
        self.homeline = homeline
        self.phone = phone
        self.email = email
        self.location = location
        #Skrá sem yfirmann? 

    def __str__(self):
        return f"name: {self.name}, ID: {self.emp_id}, Address: {self.address}, Homeline: {self.homeline}, Phone: {self.phone}, Email: {self.email}, Location: {self.location}"