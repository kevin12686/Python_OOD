def eat(p):
    p['weight'] += 1


def exercise(p):
    p['weight'] -= 1


def speak(p):
    print('%s, weight: %d' % (p['name'], p['weight']))


if __name__ == '__main__':
    person = {'name': 'Kevin',
              'weight': 50}

    speak(person)
    eat(person)
    speak(person)
    exercise(person)
    speak(person)
