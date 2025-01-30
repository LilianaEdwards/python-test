class Restaurant :
    def __init__(self,restaurant_name,cuisine_type) :
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self) :
        print(f"The restaurant name is {self.restaurant_name}.")
        print(f"It offers {self.cuisine_type} cuisin food.")
    def open_restaurant(self) :
        print(f"The {self.restaurant_name} restaurant opens from 9:00AM to 5:00PM")
    def set_number_served(self,number_served) :
        if(number_served < self.number_served) :
            print("Your input number is less than original number")
        else :
            self.number_served = number_served
            print(f"Now the number of customers is {self.number_served} now.")
    def increment_number_served(self,increment) :
        self.number_served += increment
restaurant = Restaurant('Tum Laii','Thai')
print(f"The number of customers is {restaurant.number_served}.")

restaurant.number_served = 27
print(f"The number of customers is {restaurant.number_served} now.")

number = int(input("Enter number of customers>> "))
restaurant.set_number_served(number)

restaurant.increment_number_served(10)
print(f"The final number of customers is {restaurant.number_served}")


