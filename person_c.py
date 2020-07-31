class Person:

    def __init__(self, name, weight, fat_rate=1):
        self.name = name
        self.weight = weight
        self.rate = fat_rate

    def eat(self):
        self.weight += self.rate

    def exercise(self):
        self.weight -= self.rate

    def speak(self):
        print('%s, weight: %d' % (self.name, self.weight))


if __name__ == '__main__':
    p1 = Person(name='Kevin', weight=50, fat_rate=3)
    p1.eat()
    p1.eat()
    p1.speak()
    p1.exercise()
    p1.speak()
