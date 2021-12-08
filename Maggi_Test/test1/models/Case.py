import datetime

class Case:
    def __init__(self, id, location, subject, description, priority, repeated, repeat_days, real_est_id, emp_id, date = None, status = 'Open', closed_date = None):
        self.id = id
        self.location = location
        self.subject = subject
        self.description = description
        self.priority = priority
        self.repeated = repeated
        self.repeat_days = repeat_days
        self.real_est_id = real_est_id
        self.emp_id = emp_id
        if date == None:
            self.date = self.creation_date()
        else:
            self.date = date
        self.status = status
        if status == "Closed" and closed_date == None:
            self.closed_date = self.creation_date()
        else:
            self.closed_date = closed_date

    def __str__(self):
        return f"id: {self.id}, location: {self.location}, subject: {self.subject}, description: {self.description}, priority: {self.priority}, repeated: {self.repeated}, repeat_days: {self.repeat_days}, real_est_id: {self.real_est_id}, created by: {self.emp_id} creation date: {self.date}, status: {self.status}, closed date: {self.closed_date}"
    
    def creation_date(self):
        dt = datetime.datetime.now()
        date = "%s/%s/%s" % (dt.day, dt.month, dt.year)
        return date