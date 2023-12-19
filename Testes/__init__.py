#Atividade P001
from abc import ABC, abstractmethod
from typing import List

class Data:
    
    def __init__(self, dia=1, mes=1, ano=2000):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, dia):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, mes):
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano
    
    def __str__(self):
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        return  self.__dia == outraData.__dia and \
                self.__mes == outraData.__mes and \
                self.__ano == outraData.__ano
    
    def __lt__(self, outraData):
        if self.__ano < outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes < outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia < outraData.__dia:
                    return True
        return False
    
    def __gt__(self, outraData):
        if self.__ano > outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes > outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia > outraData.__dia:
                    return True
        return False

class AnaliseDados(ABC):
    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados

    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def mostraMediana(self):
        pass
    
    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass
    
    @abstractmethod
    def listarEmOrdem(self):
        pass

class ListaNomes(AnaliseDados):
    
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []        

    def entradaDeDados(self, nome):
        self.__lista.append(nome)

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
        print("Lista de Nomes em Ordem:")
        for nome in sorted(self.__lista):
            print(nome)

    def __iter__(self):
        return iter(self.__lista)

    def __str__(self):
        return str(self.__lista)

class ListaDatas(AnaliseDados):
    
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []        

    def entradaDeDados(self, data):
        self.__lista.append(data)

    def mostraMediana(self):
        self.__lista.sort(key=lambda x: (x.ano, x.mes, x.dia))
        mediana = self.__lista[len(self.__lista)//2]
        print("Mediana:", mediana)

    def mostraMenor(self):
        menor = min(self.__lista)
        print("Menor:", menor)

    def mostraMaior(self):
        maior = max(self.__lista)
        print("Maior:", maior)

    def listarEmOrdem(self):
        print("Lista de Datas em Ordem:")
        for data in sorted(self.__lista):
            print(data)

    def atualizarDiasAntes2019(self):
        for data in self.__lista:
            if data.ano < 2019:
                data.dia = 1

    def __iter__(self):
        return iter(self.__lista)

    def __str__(self):
        return '\n'.join(map(str, self.__lista))

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

