class Auto:
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estate = 'stop'
        self._engine = Engine(cilindre=4)

    def speed_up(self, type='slow'):
        if type == 'quick':
            self._engine.refuel(10)
        else:
            self._engine.refuel(5)
        self._state = 'movement'



class Engine:
    def __init__(self, cilindre, type='gasoil'):
        self.cilindre = cilindre
        self.type = type
        self._temperature = 0

    def refuel(self, litre):
        pass
        




if __name__ == '__main__':
    pass