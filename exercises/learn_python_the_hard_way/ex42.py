## Animal is-a object (yes, sort of confusing) look at extra credit
class Animal(object):
	def hi_there(self):
		print "Hi There!"

## Dog is-a Animal
class Dog(Animal):
	def __init__(self, name):
		##  dog has-a name
		self.name = name

## cat is-a Animal
class Cat(Animal):
	def __init__(self, name):
		## cat has-a name
		self.name = name

## Person is-a object
class Person(object):
	def __init__(self, name):
		## person has-a name
		self.name = name
	
		## Person has a pet of some kind
		self.pet = None
	
## Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		## employee has-a name
		super(Employee, self).__init__(name)
		
		## employee has-a salary
		self.salary = salary

## Fish is-a object		
class Fish(object):
	pass

## salmon is-a Fish
class Salmon(Fish):
	pass

## Halibut is-a Fish
class Halibut(Fish):
	pass
	
## rover is-a dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## Mary is-a Persom
mary = Person("Mary")

## Mary has pet - Satan
mary.pet = satan

## Frank is-a employee
frank = Employee ("Frank", 120000)

## Frank has-a pet Rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()

rover.hi_there()
