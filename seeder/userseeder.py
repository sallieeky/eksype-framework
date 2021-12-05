from helper.hash import Hash
from model.user import User


class Userseeder:
    def __init__(self):
        pass

    def seed():
        User().create({
            'username': 'admin',
            'password': Hash.encrypt('admin'),
        })

        User().create({
            'username': 'eky',
            'password': Hash.encrypt('eky'),
        })
