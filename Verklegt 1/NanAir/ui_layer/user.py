class User:
    def __init__(self, user_id):
        self.user_id = user_id
        

    def is_supervisor(self):
        return self.user_id == 'sup'