from classData import Data
from classData import AnaliseDados

class ListaIdades(AnaliseDados):
    
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []        

    def entradaDeDados(self, idade):
        self.__lista.append(idade)

    def mostraMediana(self):
        self.__lista.sort()
        mediana = self.__lista[len(self.__lista)//2]
        print("Mediana:", mediana)

    def mostraMenor(self):
        menor = min(self.__lista)
        print("Menor:", menor)

    def mostraMaior(self):
        maior = max(self.__lista)
        print("Maior:", maior)

    def listarEmOrdem(self):
        print("Lista de Idades em Ordem:")
        for idade in sorted(self.__lista):
            print(idade)

    def __iter__(self):
        return iter(self.__lista)

    def __str__(self):
        return str(self.__lista)