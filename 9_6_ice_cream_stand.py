class Restaurant :
    def __init__(self,restaurant_name,cuisine_type) :
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self) :
        print(f"The restaurant name is {self.restaurant_name}.")
        print(f"It offers {self.cuisine_type} cuisine food.")
    def open_restaurant(self) :
        print(f"The {self.restaurant_name} restaurant opens from 9:00AM to 5:00PM")

class IceCreamStand(Restaurant) :
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    def show_flavors(self) :
        print("The available flavors are:")
        for flavor in flavors :
            print(flavor)
flavors = ['chocolate','vanilla','strawberry','banana']
IceCreamStand.show_flavors(flavors)