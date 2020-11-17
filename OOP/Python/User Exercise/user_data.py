class User(object):
    """Class for user's details"""
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age

        def __repr__(self):
            return self.username
