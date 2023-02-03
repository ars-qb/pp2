from datetime import datetime
from hashlib import sha256

class User:

    def __init__(self, name, birth, login, password):
        self.name = name
        self.birth = birth
        self.login = login
        self.password = sha256(password.encode('utf-8')).hexdigest()

    def age(self):
        return (datetime.now().year - self.birth)

    def info(self):
        return {"Name": self.name,
                "Login": self.login,
                "Age": self.age(),
                "Password": self.password
                }

class Registration(User):
    def __init__(self):
        self.get_name()
        self.get_login()
        self.get_birth()
        self.get_pass()

        super().__init__(self.name, self.birth, self.login, self.password)

    def get_name(self):
        self.name =  input("Name: ")
    def get_login(self):
        self.login = input("Login: ")
    def get_birth(self):
        birth = input("Year of Birth: ")
        try: self.birth = int(birth)
        except:
            print("Enter correct Year: ")
            self.get_birth()

    def get_pass(self):
        password1 = input("Password: ")
        password2 = input("Re-type Password: ")
        if password1 == password2:
            self.password = password1
        else:
            print("Password does not match")
            self.get_pass()

x = Registration()
print("Your info: ")
print(x.info())









