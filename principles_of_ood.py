class Bird:

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def describe(self, full=False):
        return f'Размер птицы {self.name} — {self.size}.'


class Parrot(Bird):

    def __init__(self, name, size, color):
        super().__init__(name, size)
        self.color = color

    def describe(self, full):

        if full False:
            return f'Размер птицы {self.name} — {self.size}.'
        else:
            return (
                    f'Попугай {self.name} — заметная птица,'
                    f' окрас её перьев — {self.color}, '
                    f'а размер — {self.size}.'
                    f' Интересный факт: попугаи чувствуют ритм, '
                    f' а вовсе не бездумно двигаются под музыку.'
                    f' Если сменить композицию, то и темп движений  '
                    f' изменится.'
                )

    # Переопределите метод describe().


class Penguin(Bird):
    def __init__(self, name, size, genus):
        super().__init__(name, size)
        self.genus = genus

    def describe(self, full):
        if full False:
            return f'Размер птицы {self.name} — {self.size}.'
        else:
            return (
                   f'Размер пингвина name из рода genus — {self.size}. '
                   f' Интересный факт: однажды группа геологов-разведчиков '
                   f' похитила пингвинье яйцо, и их принялась преследовать '
                   f' вся стая, не пытаясь, впрочем, при этом нападать. '
                   f' Посовещавшись, похитители вернули птицам яйцо, и те '
                   f' отстали.'
                )
    # Переопределите метод describe().


kesha = Parrot('Ара', 'средний', 'красный')
kowalski = Penguin('Королевский', 'большой', 'Aptenodytes')

# Вызов метода у созданных объектов.
print(kesha.describe())
print(kowalski.describe(True))
