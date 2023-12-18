from classData import Data
from classData import AnaliseDados

class ListaSalarios(AnaliseDados):

    def __init__(self):
        super().__init__(type(float))
        self.__lista = []        

    def entradaDeDados(self, salario):
        self.__lista.append(salario)

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
        print("Lista de Salários em Ordem:")
        for salario in sorted(self.__lista):
            print(salario)

    def __iter__(self):
        return iter(self.__lista)

    def __str__(self):
        return str(self.__lista)