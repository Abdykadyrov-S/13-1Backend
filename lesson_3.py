# Полиморфизм и Инкапсуляция

# Полиморфизм

# class Animal:
#     def __init__(self, name, color):
#           self.name = name
#           self.color = color
#           self.age = 0
    
#     def info_about_animal(self):
#         print(f"имя - {self.name}, цвет - {self.color}")
        
#     def speak(self):
#         pass


# class Dog(Animal):
#      def __init__(self, name, color):
#           Animal.__init__(self, name, color)
        
#      def speak(self):
#          print("Gaf-Gaf")

# class Cat(Animal):
#      def __init__(self, name, color):
#           Animal.__init__(self, name, color)

#      def speak(self):
#          print("Meow")

# class Cow(Animal):
#      def __init__(self, name, color):
#           Animal.__init__(self, name, color)

#      def speak(self):
#          print("Moo")


# dog = Dog("Sharik", "Black")
# cat = Cat("Murzik", "Milkyway")
# cow = Cow("Murka", "Brown")

# cow.speak()
# dog.speak()
# cat.speak()


# class Toys:
#     def __init__(self ):
#         pass

#     def play(self):
#         pass

# class CarToys(Toys):
#     def __init__(self):
#         pass

#     def play(self):
#         print("Едет")

# class DollToys(Toys):
#     def __init__(self):
#         pass

#     def play(self):
#         print("говорить")

# car = CarToys()
# car.play()

# doll = DollToys()
# doll.play()

#  Инкапсуляция

# class SmartPhone:
#     def __init__(self, sim_cards, battery):
#         self.__sim_cards = sim_cards # Приватный атрибут
#         self._battery = battery # Защищенный атрибут

#     def __info(self):
#         print(f"{self.__sim_cards}, {self._battery} - mh")

#     @property
#     def info(self):
#         return self.__info

#     @property
#     def sim_cards(self):
#         return self.__sim_cards
    

#     @sim_cards.setter
#     def sim_cards(self, new_sim_cards):
#         self.sim_cards = new_sim_cards


# mi = SmartPhone(["Beeline", "Tele2"], 5000)
# mi.info()

# # Декораторы
def first_decorator(func):
    def write():
        print("Hello world!")
        func()
        print("Bye")
    return write

@first_decorator
def hi():
    print("Hi")
hi()