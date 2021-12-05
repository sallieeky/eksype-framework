import bcrypt


class Hash:
    def __init__(self):
        pass

    def encrypt(data):
        return bcrypt.hashpw(bytes(data.encode()), bcrypt.gensalt())

    def decrypt(data, hash_data):
        return bcrypt.checkpw(bytes(data.encode()), hash_data.encode())
