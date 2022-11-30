
class parent:
    def method(self):
        print("parent")
class child(parent): # Derived class / child class
    def method2(self):
        print("child")
obj1=child()
obj1.method1()
obj1.method2()

class Dog(Animal):
    def bark(self):
        print("dog barking")
class DogChild(Dog):
    def eat(self):
        print("Eating bread..")
d = DogChild()

d=Dog()
d.bark()
d.spaek()
d.eat()