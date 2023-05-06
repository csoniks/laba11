def z1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f"название ресторана: {self.restaurant_name}, кухня: {self.cuisine_type}")

        def open_restaurant(self):
            print("ресторан открыт")

    NewRestaurant = Restaurant("Toscana", "итальянская кухня")
    print(NewRestaurant.restaurant_name, NewRestaurant.cuisine_type) #атрибуты нашего экземпляра
    NewRestaurant.describe_restaurant()#методы для нашего экземпляра
    NewRestaurant.open_restaurant()#методы для нашего экземпляра

def z2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"название ресторана: {self.restaurant_name}, кухня: {self.cuisine_type}")

        def open_restaurant(self):
            print("ресторан открыт")
    NewRestaurant1 = Restaurant(input("Введите название"), input("Введите кухню"))
    NewRestaurant2 = Restaurant("Шашлыкоф", "грузинская кухня")
    NewRestaurant3 = Restaurant("Забой", "русская кухня")
    NewRestaurant1.describe_restaurant()
    NewRestaurant2.describe_restaurant()
    NewRestaurant3.describe_restaurant()


def z3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print(f"название ресторана: {self.restaurant_name}, кухня: {self.cuisine_type}, рейтинг : {self.rating}")

        def open_restaurant(self):
            print("ресторан открыт")

        def change_rating(self):
            newrating = input("введите рейтинг")
            self.rating = newrating


    NewRestaurant = Restaurant("Toscana", "итальянская кухня", "9.5") #экземпляр
    NewRestaurant.describe_restaurant()
    NewRestaurant.change_rating()
    NewRestaurant.describe_restaurant()
z1()
z2()
z3()