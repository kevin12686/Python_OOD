class Person:

    def __init__(self, name, weight, height=180, fat_rate=1):
        self.name = name
        self.weight = weight
        self.height = height
        self.rate = fat_rate

    def eat(self):
        self.weight += self.rate

    def exercise(self):
        self.weight -= self.rate

    def speak(self):
        print('%s, weight: %d' % (self.name, self.weight))

    def health_check(self):
        return self.weight, self.height


def bmi(w, h):
    print('BMI: %f' % (w / (h / 100) ** 2))


if __name__ == '__main__':
    p1 = Person(name='Kevin', weight=50, fat_rate=3)
    p1.eat()
    p1.eat()
    p1.speak()
    p1.exercise()
    p1.speak()
    w, h = p1.health_check()
    bmi(w, h)

    p2 = Person(name='Tim', weight=40, fat_rate=1)
    p2.eat()
    p2.eat()
    p2.speak()
    p2.exercise()
    p2.speak()
    w, h = p2.health_check()
    bmi(w, h)

    p3 = Person(name='Jack', weight=20, fat_rate=2)
    p3.eat()
    p3.eat()
    p3.speak()
    p3.exercise()
    p3.speak()
    w, h = p3.health_check()
    bmi(w, h)
