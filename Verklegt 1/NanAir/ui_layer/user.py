class User:
    def __init__(self, user):
        self.user = user
    
    def is_supervisor(self):
        if self.user.supervisor == "yes":
            return True
        return False