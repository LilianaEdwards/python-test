class Restaurant :
    def __init__(self,restaurant_name,cuisine_type) :
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self) :
        print(f"The restaurant name is {self.restaurant_name}.")
        print(f"It offers {self.cuisine_type} cuisin food.")
    def open_restaurant(self) :
        print(f"The {self.restaurant_name} restaurant opens from 9:00AM to 5:00PM")
restaurant = Restaurant('Tum Laii','Thai')
print(f"The restaurant name is {restaurant.restaurant_name}")
print(f"The cuisine type is {restaurant.cuisine_type}")
restaurant.describe_restaurant()
restaurant.open_restaurant()