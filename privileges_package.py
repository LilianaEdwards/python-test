from user_package import User
class Admin(User) :
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges()
    
class Privileges :
    def __init__(self):
        self.privileges = ['can add post','can delete post','can ban user','can add user']
    def show_privileges(self) :
        print("The administrator's set of privileges are as follows:")
        for privilege in self.privileges :
            print(f"The admin {privilege}.")