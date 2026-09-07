class animal:
    def eat(self):
        print("animal eat food")
class dog(animal):
    def speak(self):
        print("bow bow")
d1 = dog()
d1.eat()
d1.speak()