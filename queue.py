from time import time

class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        self.items.pop(0)
    
    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


"""
Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and dequeueCat.

"""


class Animal:

    def __init__(self, name, order=None):
        self.name = name
        self.order = order

    def is_older_than(self, animal):
        return self.order < animal.order
    

    def __str__(self):
        return f'[name: {self.name} order: {self.order}]'


class Dog(Animal):
    def __init__(self, name, order=None):
        super().__init__(name, order)


class Cat(Animal):
    def __init__(self, name, order=None):
        super().__init__(name, order)

    


class AnimalQueue:
    
    def __init__(self, dogs,cats):
        self.dogs = dogs
        self.cats = cats

    
    def enqueue(self, animal):

        animal.order = time()

        if isinstance(animal,Dog):
            dogs.enqueue(animal)

        if isinstance(animal,Cat):
            cats.enqueue(animal)
        

    def dequeue(self):
        dog = self.dogs.peek()
        cat = self.cats.peek()

        if dog.is_older_than(cat):
            dogs.dequeue()
        else:
            cats.dequeue()

    def show_shelter(self):
        print("dogs:", *dogs.items, sep=", ")
        print("cats:", *cats.items, sep=", ")
        


dogs = Queue()
cats = Queue()

shelter = AnimalQueue(dogs=dogs, cats=cats)



golden = Dog("golden")
labrador = Dog("labrador")
bulldog = Dog("bulldog")
mastiff = Dog("mastiff")
shepherd = Dog("shepherd")


snowshoe = Cat("snowshoe")
british = Cat("british")
siamese = Cat("siamese")
norwegian = Cat("norwegian")
bobtail = Cat("bobtail")


shelter.enqueue(golden)
shelter.enqueue(siamese)
shelter.show_shelter()
shelter.dequeue()
shelter.show_shelter()


