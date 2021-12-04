import bcrypt
from model.model import Model


class User(Model):
    def __init__(self):
        Model.__init__(self, "user")

    def authenticate(self, username, password):
        user = self.whereOnly("username", "=", username)
        if user != None:
            db_pass = user["password"]
            if bcrypt.checkpw(bytes(password.encode()), db_pass.encode()):
                return True
            else:
                return False
