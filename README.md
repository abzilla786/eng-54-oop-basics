# oop basics

this repo will contain our oop basics.

we will look at: 
- Abstraction
- Encapsulation
- Inheritance
- Polymorphism

## Class
is like a cookie cutter that creates instances of cookies.

They use wrappers to define how an object looks and behaves.

Classes will wrap characteristics as attributes, and behaviours ad methods.

## Method vs Functions
Methods are functions that belong to a specific data type

Where functions are anonymous and anything can call and run them.

where as **methods need the instance to be called**

## Characteristics / how an object looks like
these are attributes that are assigned to each instance.
they are variables assigned to an object / instance

## Instances
occurrence of something.

## Self
Refers to the instance of the object f on which a method is being called

self.name = 'ringo'

this means that specific object attribute name will have the string 'ringo'

## Abstraction
The ability to hide complexity
We do this using:
- separation of concerns
- documentation
    - specify which methods and how to use them
- inheritance---> causes some abstraction

real life examples are everywhere:
- changing gears
- heating up food with one button
- using our cards to pass security

## Encapsulation
making method or attributes private.

when method or attributes are private, they can only be called by it own functions or within a class

Example:


## Inheritance
is the ability to pass to child class all the methods and characteristics.
this is one of the big reasons for OOP - it means you can re-use code!

**promise of reusable code**
you do this by passing the oarent class as an arguent of the child class

```python
class Animal():
    pass
class Reptile(Animal):
```
## Polymorphism
literally means: 
- many forms

it is the ability to COMPLETELY override methods, and if need be, recall method from parent class using 
.super()

## .super()
it represents the parent class, allows you to call methods from parent class.

Usage and case in point:
- situation where you want to overwrite a method (say method .honk() or make a sound())
- you want to add new functionality to the new method
- but still have everything from first method

--->> then you call super() :)

most of the times this happenes with the __init__ method
- you want to add new characteristics to child object
- and you want to keep all the original characteristics
- so you overwrite the init method and still call the original init method, with all necessary arguments

```python
class animal():
    
    # original init method with age and colour_fur
    def __init__(self, age, colour_fur):
        self.age = age
        self.colour_fur = colour_fur

class reptile(animal):
    
    #this overwrites the original init method
    # however what we want is to keep al the original code and add more
    def __init__(self, name, age, colour_fur):
        # use super to call original init method
        # we need to pass the arguments for the original init to work
        super().__init__(age, colour_fur) # line that runs original init with original arguments
        self.name = name

rt = reptile('ringo', 10, 'shiny gold')
```