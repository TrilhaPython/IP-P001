from classData import Data
from classAnaliseDados import AnaliseDados

class ListaSalarios(AnaliseDados):

    def __init__(self):
        super().__init__(type(float))
        self.__lista = []        

    def entradaDeDados(self, salario):
        self.__lista.append(salario)

    def mostraMediana(self):
        self.__lista.sort()
        mediana_index = len(self.__lista) // 2
        mediana = self.__lista[mediana_index]
        return mediana

    def mostraMenor(self):
        menor = min(self.__lista)
        return menor

    def mostraMaior(self):
        maior = max(self.__lista)
        return maior

    def listarEmOrdem(self):
        lista_ordenada = sorted(self.__lista)
        return lista_ordenada

    def __iter__(self):
        return iter(self.__lista)

    def __str__(self):
        return '\n'.join(str(salario) for salario in self.__lista)