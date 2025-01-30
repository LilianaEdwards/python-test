class Restaurant :
    def __init__(self,restaurant_name,cuisine_type) :
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self) :
        print(f"The restaurant name is {self.restaurant_name}.")
        print(f"It offers {self.cuisine_type} cuisin food.")
    def open_restaurant(self) :
        print(f"The {self.restaurant_name} restaurant opens from 9:00AM to 5:00PM")
restaurant1 = Restaurant('Tum Laii','Thai')
restaurant1.describe_restaurant()
restaurant2 = Restaurant('Golden Duck','Chinese')
restaurant2.describe_restaurant()
restaurant3 = Restaurant('Mingalarpar','Myanmar')
restaurant3.describe_restaurant()
