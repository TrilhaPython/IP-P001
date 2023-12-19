# Tutorial: Configuração do Ambiente Virtual para Projetos no Windows

Neste tutorial, vamos abordar a criação de um ambiente virtual isolado utilizando as ferramentas estudadas em sala de aula. O objetivo é fornecer um ambiente controlado para o desenvolvimento de projetos complexos, usando Jupyter Notebooks para aulas e prototipação, e Visual Studio Code (VSCode) para o desenvolvimento de aplicações, módulos e pacotes.

## Passo 1: Instalação das Ferramentas Necessárias

Certifique-se de ter as seguintes ferramentas instaladas em seu sistema:

- **Python**: Instale a versão mais recente do Python, disponível em [python.org](https://www.python.org/).
- **VSCode**: Baixe e instale o Visual Studio Code do site oficial: [Visual Studio Code](https://code.visualstudio.com/).
- **Jupyter Notebook**: Instale o Jupyter Notebook com o comando:
  ```bash
  pip install notebook
  
  
## Passo 2: Criação do Ambiente Virtual

Abra o terminal ou prompt de comando e navegue até o diretório do seu projeto.
Execute o seguinte comando para criar um ambiente virtual:

python -m venv nome_do_ambiente
Substitua "nome_do_ambiente" pelo nome desejado para o ambiente virtual.

## Passo 3: Ativação do Ambiente Virtual

No terminal do Windows:

nome_do_ambiente\Scripts\activate


## Passo 4: Instalação de Dependências

Com o ambiente virtual ativado, instale as dependências necessárias, como o Jupyter:

pip install jupyter

## Passo 5: Integração com o VSCode

Abra o VSCode e instale a extensão "Python" para facilitar o desenvolvimento Python.
Abra o VSCode na raiz do seu projeto.

No canto inferior esquerdo, clique em "Select Python Interpreter" e escolha o interpretador do ambiente virtual criado.
## Passo 6: Integração com o Jupyter

No terminal do VSCode, certifique-se de que o ambiente virtual está ativado.
Execute o comando para iniciar o Jupyter Notebook:

jupyter notebook

O Jupyter Notebook será aberto no navegador padrão. Crie ou abra notebooks conforme necessário.
