from person_c import Person


class Batman(Person):
    def __init__(self, deposit, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.deposit = deposit

    def house(self, *args, **kwargs):
        print('buy house')


if __name__ == '__main__':
    b = Batman(100, 'Bad', 1000, height=199)
    b.speak()
    b.house()
