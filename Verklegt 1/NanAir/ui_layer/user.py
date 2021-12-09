class User:
    def __init__(self, user):
        self.user = user
        self.user_id = user.id
    
    def is_supervisor(self):
        """checks if employee is supervisor"""
        if self.user.supervisor == "yes":
            return True
        return False