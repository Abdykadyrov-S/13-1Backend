# # ООП - Объектно Ориентированое Програмирование
# # DRY - Don`t Repeat Yourself == не повтаряйся 

# class - чертеж , инструкция
# class Car:
#     wheels = 4 # Атрибут класса
#         # self - сам объект
#         # __init__ - конструктор
#     def __init__(self, model, color):
#         # self.model = model - Атрибут объекта
#         self.model = model
#         self.color = color
#         self.year = 2023
#         # pass - пропустить
    
#     def info(self):
#         print(f"Бренд машины - {self.model}, Цвет - {self.color}, Год выпуска - {self.year}")

#     def drive(self, location, speed):
#         print(f"Машина едет в {location} со скоростью {speed} км/ч")

# # экземпляры класса
# mersedes = Car("cls", "Черный")
# mersedes.info()
# mersedes.drive("Ош", 200)
# print(mersedes.wheels)
# print(mersedes.color)
# print(mersedes.year)


# bmw = Car("x-5", "Белый")
# bmw.info()
# bmw.drive("Бишкек", 200)
# print(bmw.wheels)
# print(bmw.color)
# print(bmw.year)

# bmw = Car()

# class Airplane:
#     def __init__(self, model, year, color, capacity, max_speed):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.capacity = capacity
#         self.max_speed = max_speed
#         self.is_flying = False
#         self.odometer = 0

#     def info_about_airplane(self):
#         print(f"{self.model}, {self.year}-года выпуска, цвет - {self.color}, {self.capacity} тонны, {self.max_speed} км/ч, {self.is_flying}, километраж -  {self.odometer}" )
    
#     def take_of(self):
#         self.is_flying = True
#         print("Самолет взлетел")
    
#     def fly(self, distance):
#         if self.is_flying == True:
#             self.odometer += distance
#             print(f"Самолет пролетел {distance} км")
#         else:
#             print("Сначала выполните взлет")
    
#     def to_land(self):
#         self.is_flying = False
#         print("Самолет приземлился")


# plane = Airplane("MI-38", 1992, "Комуфляж", 3, 450)
# plane.take_of()
# plane.fly(200)
# plane.to_land()
# plane.info_about_airplane()

