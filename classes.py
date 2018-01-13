#!/usr/bin/python

class Dog:

	def __init__(self, name):
		self.name = name
		self.tricks = []    # creates a new empty list for each dog

	def add_trick(self, trick):
		self.tricks.append(trick)
		
		
d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.name)
print(d.tricks)
print(e.name)
print(e.tricks)



class Bag:
	def __init__(self):
		self.data = []

	def add(self, x):
		self.data.append(x)

	def addtwice(self, x):
		self.add(x)
		self.add(x)
		
q = Bag()
q.addtwice(12)
q.add(55443345)

print(q.data)		
