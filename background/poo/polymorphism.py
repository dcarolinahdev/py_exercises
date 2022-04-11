class Person:

    def __init__(self, name):
        self.name = name

    def move(self):
        print('Ando caminando')


class Cyclist(Person):

    def __init__(self, name):
        super().__init__(name)

    def move(self):
        print('Ando moviendome en mi bicicleta')


def main():
    persona = Person('David')
    persona.move()

    ciclista = Cyclist('Daniel')
    ciclista.move()


if __name__ == '__main__':
    main()