class User :
    def __init__(self,first_name,last_name,age,gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
    def describe_user(self) :
        print("****User Profile****")
        print(f"Full Name >> {self.first_name} {self.last_name}")
        print(f"Age       >> {self.age}")
        print(f"Gender    >> {self.gender}")
    def greet_user(self) :
        print(f"Hello {self.first_name} {self.last_name}, welcome from our page!!")