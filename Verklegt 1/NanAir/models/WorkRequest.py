class WorkRequest:
    def __init__(self, description, subject, priorities, status, due_date, repeated, creation_date):
        self.subject = subject
        self.description = description
        self.priorities = priorities
        self.status = status
        self.due_date = due_date
        self.repeated = repeated
        self.creation_date = creation_date

