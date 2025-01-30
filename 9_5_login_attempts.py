class User :
    def __init__(self,first_name,last_name,age,gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0
    def describe_user(self) :
        print("****User Profile****")
        print(f"Full Name >> {self.first_name} {self.last_name}")
        print(f"Age       >> {self.age}")
        print(f"Gender    >> {self.gender}")
    def greet_user(self) :
        print(f"Hello {self.first_name} {self.last_name}, welcome from our page!!")
    def increment_login_attempts(self) :
        self.login_attempts += 1
    def reset_login_attempts(self) :
        self.login_attempts = 0
user = User('Kyaw','Kyaw',25,'Male')
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"You entered {user.login_attempts} times.")

user.reset_login_attempts()
print(f"Your login attempt was reset to {user.login_attempts} .")

