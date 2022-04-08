
class Car:

    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color
        self._status = 'resting'
        self._motor = Motor(cilindros=4)

    def acelerar(self, type='slowly'):
        if type == 'quick':
            self._motor.inject_gasoline(10)
        else:
            self._motor.inject_gasoline(3)

        self._status = 'moving'


class Motor:

    def __init__(self, cylinders, type='gasoline'):
        self.cylinders = cylinders
        self.type = type
        self._temperature = 0
        self._gasoline_lvl = 0

    def inject_gasoline(self, amount_gasoline):
        self._gasoline_lvl = self._gasoline_lvl - amount_gasoline
