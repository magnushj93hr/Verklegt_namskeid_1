class Case:
    def __init__(self, id, location, subject, description, priority, due_date, repeated):
        self.id = id
        self.location = location
        self.subject = subject
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.repeated = repeated

    def __str__(self):
        return f"id: {self.id}, location: {self.location}, subject: {self.subject}, description: {self.description}, priority: {self.priority}, due_date: {self.due_date}, repeated: {self.repeated}"