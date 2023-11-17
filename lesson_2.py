# Наследование и Абстракция

class Transport: # - Абстракция
    def __init__(self, company, capacity, max_speed, model, year):
        self.company = company
        self.capacity = capacity
        self.max_speed = max_speed
        self.model = model
        self.year = year

    def info(self):
            print(f"Компания - {self.company},{self.model}, {self.year}-года выпуска, {self.capacity} тонны, {self.max_speed} км/ч," )


class Car(Transport):
    def __init__(self, company, capacity, max_speed, model, year, wheels = 4):
        Transport.__init__(self, company, capacity, max_speed, model, year)
        self.wheels = wheels
        self.penalties = 0


    def info(self):
            print(f"Компания - {self.company},{self.model}, {self.year}-года выпуска, {self.capacity} тонны, {self.max_speed} км/ч," )

    # def drive(self, location, speed):
    #     print(f"Машина едет в {location} со скоростью {speed} км/ч")

mersedes = Car("Mersedes-Benz", 8, 300, "cls", 2023)
mersedes.info()




class Airplane(Transport):
    def __init__(self,company, model, year, capacity, max_speed):
         super().__init__(company, capacity, max_speed, model, year)
         self.is_flying = False
         self.odometer = 0


    def info(self):
        print(f"Компания - {self.company},{self.model}, {self.year}-года выпуска, {self.capacity} тонны, {self.max_speed} км/ч," )
 
    def take_of(self):
        self.is_flying = True
        print("Самолет взлетел")
    
    def fly(self, distance):
        if self.is_flying == True:
            self.odometer += distance
            print(f"Самолет пролетел {distance} км")
        else:
            print("Сначала выполните взлет")
    
    def to_land(self):
        self.is_flying = False
        print("Самолет приземлился")


plane = Airplane("MI-38", 1992, "Комуфляж", 3, 450)
plane.info()
# plane.take_of()
# plane.fly(200)
# plane.to_land()
# plane.info_about_airplane()


class Animal:
    def __init__(self, name, color):
          self.name = name
          self.color = color
          self.age = 0
    
    def info_about_animal(self):
         print(f"имя - {self.name}, цвет - {self.color}")


class Dog(Animal):
     def __init__(self, name, color, breed):
          Animal.__init__(self, name, color)
          self.breed = breed


dog = Dog("Vlad", "Белый", "human")
dog.info_about_animal()
