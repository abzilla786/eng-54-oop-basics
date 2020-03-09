from animal_class import *


class reptile(Animal):
    def __init__(self,name, age, colour, scales, blood_temp):
        super().__init__(name, age, colour)
        self.scales = scales
        self.blood_temp = blood_temp


    def make_sound(self):
        return 'zlslslslslz phyton'


animal1 = Animal('nacho', 20, 'yellowish')

reptile1 = reptile('ringo', 30, 'yellow', 'lots', 'very cold')

print(animal1)
print(reptile1)

# reptile has all the attribute and method of animal
print(reptile1.name)  # this is a attribute of reptile not a method

print(reptile1.eat())
print(reptile1.Potty())
print(reptile1.sleep())
print(reptile1.reproduce())
print(reptile1.make_sound())
