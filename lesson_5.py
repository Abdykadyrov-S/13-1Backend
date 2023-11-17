# class Phone:
#     def __init__(self, battery):
#         self.battery = battery

#     def __str__(self):
#         return f"Емкость баттареи {self.battery}"

#     # Магические методы для арифметических действий
#     def __add__(self, other): # Операция сложения == (+)
#         new_battery = self.battery + other.battery
#         return Phone(new_battery)
    
#     def __sub__(self, other): # Операция вычитания == (-)
#         new_battery = self.battery - other.battery
#         return Phone(new_battery)
    
#     def __mul__(self, other): # Операция умножения == (*)
#         new_battery = self.battery * other.battery
#         return Phone(new_battery)
    
#     def __floordiv__(self, other): # Операция деления без остатка == (//)
#         new_battery = self.battery // other.battery
#         return Phone(new_battery)
    
#     def __truediv__(self, other): # Операция деления с остатком == (/)
#         new_battery = self.battery / other.battery
#         return Phone(new_battery)
    
#     # Магические методы для операторов сравнения

#     def __gt__(self, other): # Больше чем == (>)
#         return self.battery > other.battery
    
#     def __lt__(self, other): # Меньше чем == (<)
#         return self.battery < other.battery
    
#     def __eq__(self, other): # Равно == (==)
#         return self.battery == other.battery
    
#     def __ne__(self, other): # не равно == (!=)
#         return self.battery != other.battery
    
#     def __ge__(self, other): # Больше или равно == (>=)
#         return self.battery >= other.battery
    
#     def __le__(self, other): # Меньше или равно == (<=)
#         return self.battery <= other.battery
    
#     # Магический метод __call__
#     def __call__(self):
#         print("Hello World")
#         print( self.battery <= 7)
    
# phone = Phone(2000)
# phone_2 = Phone(3000)
# print(phone)


# # Магические методы для арифметических действий
# print(phone + phone_2)
# print(phone - phone_2)
# print(phone * phone_2)
# print(phone // phone_2)
# print(phone / phone_2)

# # Магические методы для операторов сравнения
# print(phone > phone_2)
# print(phone < phone_2)
# print(phone >= phone_2)
# print(phone <= phone_2)
# print(phone == phone_2)
# print(phone != phone_2)

# phone() # __call__ 

print(__name__)
from lesson_6.folder.test import add