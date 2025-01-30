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

class Admin(User) :
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = privileges
    def show_privileges(self) :
        print("The administrator's set of privileges are as follows:")
        for privilege in privileges :
            print(f"The admin {privilege}.")

privileges = ['can add post','can delete post','can ban user','can add user']
Admin.show_privileges(privileges)