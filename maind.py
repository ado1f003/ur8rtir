#class Student:
#    amount_of_students = 0
#    def init(self, height=160):
 #       self.height = height
 #       Student.amount_of_students += 1
 #   def grow(self, height=1):
#
 #       self.height += height
#nick = Student()
#kate = Student(height=170)
#nick.grow(height=15)
#print(kate.height)
#print(nick.height)

#
# class PC:
#     cpu = 'i5 7500'
#     gpu = '3060ti'
#     ram = 16
#     power_unit = 650
#    motherboard = motherboard


# class PC:
#
#     def __init__(self, cpu, gpu, ram, ssd, power_unit, motherboard):
#         self.cpu = cpu
#         self.gpu = gpu
#         self.ram = ram
#         self.power_unit = power_unit
#         self.motherboard = motherboard
#
#     def get_info(self):
#         return f'\nCPU = {self.cpu}\n' \
#                f'Motherboard = {self.motherboard}\n' \
#                f'GPU = {self.gpu}\n' \
#                f'RAM = {self.ram}\n' \
#                f'SSD = {self.ssd}\n' \
#                f'Power unit = {self.power_unit} w'
#
# people1 = PC('i5 7500', '3060ti', 16, 512, 650, 'Asus b350')
# people2 = PC('i3 8100', '1050ti', 8, 1000, 550, 'Gigabyte b250')

from random import randint

class Player:

    HINTS = {
        'CLOSE': 20, #list(range(0, 20 + 1)),
        'NOT BAD': 40, #list(range(21, 40 + 1)),
        'QUIET BAD': 100
    }


    def __init__(self, name):
        self.name = name
        self.score = 0
        self.wins = 0

    def __str__(self):
        return f'\nname: {self.name}\nscore: {self.score}\nwins {self.wins}'

    def add_score(self):
        pass

    def set_choice(self):
        self.__choice

    def get_choice(self):
        return self.__choice



    def status_round(self, number):
        for key, value in self.HINTS.items():
            if number <= value:
                return key



a = Player('Nick')
b = Player('Joe')


rand_num = randint(0, 100)
print('rand =', rand_num)
for i in range(3):
    a.set_choice(int(input(f'{a.name}, enter answer')))
    b.set_choice(int(input(f'{b.name}, enter answer')))
    print(abs(a.get_choice() - rand_num))
    print(abs(b.get_choice() - rand_num))