from helper.hash import Hash
from model.user import User


class Userseeder:
    def __init__(self):
        pass

    def seed():
        User().create({
            'email': 'admin@eksype.com',
            'password': Hash.encrypt('admin'),
        })

        User().create({
            'email': 'eksype@eksype.com',
            'password': Hash.encrypt('eksype'),
        })
