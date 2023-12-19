from __init__ import *


def incluirNome(listaNomes):
    nome = input("Digite um nome: ")
    listaNomes.entradaDeDados(nome)

def incluirSalario(listaSalarios):
    salario = float(input("Digite um salário: "))
    listaSalarios.entradaDeDados(salario)

def incluirData(listaDatas):
    dia = int(input("Dia: "))
    mes = int(input("Mês: "))
    ano = int(input("Ano: "))
    data = Data(dia, mes, ano)
    listaDatas.entradaDeDados(data)

def incluirIdade(listaIdades):
    idade = int(input("Digite uma idade: "))
    listaIdades.entradaDeDados(idade)

def percorrerListas(listaNomes, listaSalarios):
    print("Iterador zip:")
    for nome, salario in zip(listaNomes, listaSalarios):
        print(f"{nome}: {salario}")

def calcularReajuste(listaSalarios):
    print("Iterador map:")
    salarios_reajustados = map(lambda x: x * 1.1, listaSalarios)
    print(list(salarios_reajustados))

def modificarDiasAntes2019(listaDatas):
    print("Iterador filter:")
    listaDatas.atualizarDiasAntes2019()
    for data in listaDatas:
        print(data)

def Menu():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    while True:
        print("\nMenu:")
        print("1. Incluir um nome na lista de nomes")
        print("2. Incluir um salário na lista de salários")
        print("3. Incluir uma data na lista de datas")
        print("4. Incluir uma idade na lista de idades")
        print("5. Percorrer as listas de nomes e salários")
        print("6. Calcular o valor da folha com um reajuste de 10%")
        print("7. Modificar o dia das datas anteriores a 2019")
        print("8. Sair")

        escolha = input("Escolha uma opção (1-8): ")

        if escolha == '1':
            incluirNome(nomes)
        elif escolha == '2':
            incluirSalario(salarios)
        elif escolha == '3':
            incluirData(datas)
        elif escolha == '4':
            incluirIdade(idades)
        elif escolha == '5':
            percorrerListas(nomes, salarios)
        elif escolha == '6':
            calcularReajuste(salarios)
        elif escolha == '7':
            modificarDiasAntes2019(datas)
        elif escolha == '8':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    Menu() 