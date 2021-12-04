import bcrypt

passwd = b'eky12345'

salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(passwd, salt)

print(hashed)

if bcrypt.checkpw(b"eky12345", hashed):
    print("match")
else:
    print("does not match")
