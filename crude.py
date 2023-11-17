import mysql.connector
from datetime import datetime

"""Dados de entrada:alunos, modalidade, personal, funcionarios
Menu: inserir atualizar, deletar, visualizar. escolher a tabela que será feita a alteração"""
import mysql.connector
from bliblioteca_banco_dados import *

# Conectar ao banco de dados


while True:
    conexao = mysql.connector.connect(
        host="localhost", user="root", password="root", database="supermercado"
    )
    tabela = input("Qual tabela ira usar?1-produtos 2-funcionarios 3-setores 4-sair")

    if tabela == "3":
        escolha = input("digite a-atualizar d-deletar, v-visualizar")

        v1 = input("Qual o nome do setor ira ser cadastrado?")
        criar(conexao, tabela, v1)

        if escolha == "v":
            leia = input("o que deseja ler?")

            ler(conexao, leia)
        elif escolha == "d":
            tabela_s = input("selecione qual a tabela ira apagar")
            id = int(input("id da tabela"))
            deletar(conexao,tabela, id)
        elif escolha == "a":
            tabela = input("qual tabela deseja alterar?")
            id = int(input("Qual o id da tabela?"))
            coluna = input("Selecione a coluna")
            novo_valor = input("Novo valor")
            atualizar(conexao,tabela,id,coluna,novo_valor)




    elif tabela == "4":
        break
    elif tabela == "2":
        leia = "funcionarios"
        v1 = input("Qual o nome do funcionario?")
        v2 = float(input("Qual o salario  ira ser cadastrado?"))
        criar(conexao, tabela, v1, v2)
        ler(conexao, leia)

    else:
        leia = "produtos"
        v1 = input("Qual o nome do produto?")
        v2 = str(input("Qual a data de validade?Use o formato YYYY-MM-DD"))
        v3 = float(input("Qual o preço cadastrado?"))

        criar(conexao, tabela, v1, v2, v3)
        ler(conexao, leia)


conexao.close()
