# Animal is-a object (yes, sort of confusing)
class Animal(object):
    pass

##Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
        ## dog has-a name
        self.name = name

#Cat is-a animal
class Cat(Animal):
    def __init__(self, name):
        # has-a name
        self.name = name
        
# Person is-a object
class Person(object):
    def __init__(self, name):
        # has-a name
        self.name = name
        
        #Person has-a pet
        self.pet = None
        
#Employee is-a person
class Employee(Person):
    def __init__(self, name, salary):
        #call parent constructor
        super(Employee, self).__init__(name)
        # Employee has-a salary
        self.salary = salary
        
class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass
    
##rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

#mary is a person
mary = Person("Mary")
#mary has-a cat
mary.pet = satan

#frank is-a employee
frank = Employee("Frank", 120000)

#frank has-a pet
frank.pet = rover

#flipper is-a fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

#harry is a halibut
harry = Halibut()
