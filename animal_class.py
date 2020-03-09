# define our animal class

# sudo
# looks / characteristics of every animal
# name, age, colour, heart, brain

# Behaviour / Methods of every animal
# eat, sleep, reproduce, potty, make_sound

class Animal():
    # Define behaviour and characteristics

    # define the characteristic of every animal
    def __init__(self, name, age_days, colour):
        self.__age_days = age_days
        self.name = name
        self.colour = colour
        self.heart = True
        self.brain = True
        self.skills = {}

    # age
    # we should be able to retrieve the age
    # a user should not be able to set his/her own age
    # however as the animal sleeps, it should increment the age

    # first lets make the age private
    # create a method that gets the age and returns it
    def get_age(self):  # a greater method - allows access to encapsulated resources
        return self.__age_days  # inside the class we have access to the private methods.

    # change the sleep method to increment the age

    def set_age(self, __age_days):
        # we should not be able to change / alter the age without being an admin

        # fake verification
        password = input('what is the password')

        if password == 'Supersecret: ':
            self.__age_days = __age_days
            return True
        else:
            return False


    # Defining a method .eat(), .sleep(), .reproduce()
    def __increment_age(self):
        self.__age_days += 1
        
    def eat(self):
        # when it eats it should increment the age
        # we will do this by calling the __incremenet_age() method
        return 'nom nom nom'

    def sleep(self):
        return 'ZzzzzzZZZzzZZZZZzz'

    def reproduce(self):
        return 'I\'m going to need some privacy here...: '

    def Potty(self):
        return ' 0_0 HUMMM! KAKA'

    def make_sound(self):
        return 'WOOF HEWWWW MEWOOOO!'


# To call methods we need an object of this class
# To create an instance of class animal
ringo = Animal('ringo', 300, 'blueish')  # creates instances of class animal and assigns to variable ringo

# me having all access to age_days
# i can print it
# print(ringo.__age_days())

# i can even modify it!
# ringo.__age_days = 'hello'
# print(ringo.__age_days)
print(ringo.get_age())
print(ringo.set_age(500))
print(ringo.get_age())

# checking and print the instance
# print(ringo)
# print(type(ringo))
#
# # calling methods on instance of animal
# print(ringo.eat())
# print(ringo.Potty())
# print(ringo.sleep())
#
# # check the attributes of an animal
# print(ringo.name)
# print(ringo.__age_days)
#
# # second animal
# mini = Animal('Stacy', 450, 'green')
#
# print(mini.name)
