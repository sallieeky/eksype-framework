import os
cek = ""
module = []
try:
    import PyQt5
except:
    cek += "\tPyQt5\n"
    module.append("PyQt5")

try:
    import pymysql
except:
    cek += "\tpymysql\n"
    module.append("pymysql")

try:
    import bcrypt
except:
    cek += "\tbcrypt\n"
    module.append("bcrypt")

if cek != "":
    print("\nThe following modules are missing:")
    print(cek)
    install = input("\nDo you want to install them? (y/n) ")
    if install == "y":
        for i in module:
            os.system("pip install "+i)
        print("\nDone!")
    else:
        print("\nYou need to install the modules first to run the program!")

else:
    print("\nAll modules are installed.")
    print("\nNow you can run the program.")
