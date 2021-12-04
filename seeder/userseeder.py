from model.user import User
import bcrypt


class Userseeder:
    def __init__(self):
        pass

    def seed():
        User().create({
            'username': 'admin',
            'password': bcrypt.hashpw(b"admin", bcrypt.gensalt()),
        })
