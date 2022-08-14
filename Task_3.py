class Tomato:
    states = {1: 'new', 2: 'mid', 3: 'ripe'}

    def __init__(self, index):
        self.__index = index
        self.__state: str = Tomato.states[1]

    def grow(self):
        if self.__state == 'new':
            self.__state = Tomato.states[2]
        elif self.__state == 'mid':
            self.__state = Tomato.states[3]

    def is_ripe(self):
        return self.__state == 'ripe'


class TomatoBush:

    def __init__(self, num_of_t):
        self.tomatoes = [Tomato(i) for i in range(num_of_t)]

    def grow_all(self):
        for t in self.tomatoes:
            t.grow()

    def all_are_ripe(self):
        for t in self.tomatoes:
            if not t.is_ripe():
                return False
        return True

    def give_away_all(self):
        self.tomatoes.clear()


class Gardener:

    def __init__(self, name, tomato: Tomato):
        self.name = name
        self.__plant = tomato

    def work(self, bush: TomatoBush):
        bush.grow_all()

    def harvest(self, bush: TomatoBush):
        if bush.all_are_ripe():
            bush.give_away_all()
            return True
        else:
            print('Not all tomatoes are ripe!')
            return False

    @staticmethod
    def knowledge_base():
        print('''Класс Tomato:
статическое свойство states - все стадиисозревания помидора
 метод __init__()определены два динамических protected свойства: 1) _index - передается параметром и 2) _state - принимает первое
значение из словаря states
метод grow() переводит томат на следующую стадию созревания
is_ripe()проверяtn, что томат созрел (достиг последней стадии созревания)
Класс TomatoBush
метод __init__()принимать в качестве параметра количество томатов и на его основе будет создавать список объектов класса
Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
метод grow_all(), который переводит все объекты из списка томатов на следующий этап созревания
метод all_are_ripe() возвращаtn True, если все томаты из
списка стали спелыми
метод give_away_all() будет чистить список томатов после сбора урожая
Класс Gardener
метод __init__(), внутри которого определены два динамических
свойства: 1) name - передается параметром, является публичным и 2) _plant -
принимает объект класса Tomato, является protected
work(), который заставляет садовника работать, что позволяет
растению становиться более зрелым
harvest(), который проверяет, все ли плоды созрели. Если все -
садовник собирает урожай. Если нет - метод печатает предупреждение.
статический метод knowledge_base(), который выведет в консоль справку
по садоводству.''')


def main():
    Gardener.knowledge_base()
    bush_1 = TomatoBush(5)
    tomato_1 = Tomato(1)
    gardener_1 = Gardener('Den', tomato_1)
    gardener_1.work(bush_1)
    while not gardener_1.harvest(bush_1):
        gardener_1.work(bush_1)


main()
