import datetime

class Case:
<<<<<<< Updated upstream
    def __init__(self, id, location, subject, description, priority, repeated, real_est_id, date = None):
=======
    def __init__(self, id, location, subject, description, priority, due_date, repeated, reports = []):
>>>>>>> Stashed changes
        self.id = id
        self.location = location
        self.subject = subject
        self.description = description
        self.priority = priority
        self.repeated = repeated
<<<<<<< Updated upstream
        if date == None:
            self.date = self.creation_date()
        else:
            self.date = date
        self.real_est_id = real_est_id
=======
        self.reports = reports
>>>>>>> Stashed changes

    def __str__(self):
        return f"id: {self.id}, location: {self.location}, subject: {self.subject}, description: {self.description}, priority: {self.priority}, repeated: {self.repeated}, creation date: {self.date}, real_est_id: {self.real_est_id}"
    
    def creation_date(self):
        dt = datetime.datetime.now()
        date = "%s/%s/%s" % (dt.day, dt.month, dt.year)
        return date