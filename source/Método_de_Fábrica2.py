from abc import ABCMeta, abstractmethod

class Firma():
    __metaclass__ = ABCMeta

    @abstractmethod
    def describe(self):
        pass


class Transporte(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        self.transportes = []
        self.create_transporte()

    @abstractmethod
    def create_transporte(self):
        pass

    def get_transportes(self):
        return [type(t).__name__ for t in self.transportes]

    def atr_transporte(self, transporte):
        self.transportes.append(transporte)


class Navio(Transporte):

    def describe(self):
        print('Navio')


class Caminhao(Transporte):

    def describe(self):
        print('Caminhão')
        

if __name__ == '__main__':

    c = Caminhao()
    n = Navio()

    

    print('Meio de Transporte...', type(c).__name__)
    #print('Transporte para --', c.get_transportes())

    print('Meio de Transporte...', type(n).__name__)
    #print('Transporte para --', n.get_transportes())