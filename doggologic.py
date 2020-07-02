from random import seed
from random import randint
import dognames as names 

class Dog(object):
	global dogdata
	seed(100)
	dogdata=[]

	def __init__(self, breed, age, gender):
		self.breed=breed
		self.age=age
		self.gender=gender
		self.beauty=randint(1,100)
		self.happiness=randint(1,100)
		self.ls=randint(1,10)
		self.counter=0
		self.counter+=1
		self.dataset={"counter":self.counter, "breed":self.breed, "age":self.age, "gender":self.gender, "beauty":self.beauty, "happiness":self.happiness, "ls":self.ls}
		dogdata.append(self.dataset)
		self.status=0
		
Guru=Dog(breed="GS", age="16", gender="Male")
daisy=Dog(breed="GS", age="14", gender="Female")

print("Guru is {} points happy!".format(Guru.happiness))
