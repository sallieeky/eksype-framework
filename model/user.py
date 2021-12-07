from model.model import Model


class User(Model):
    def __init__(self):
        Model.__init__(self, "user")
        self.auth = "email"
