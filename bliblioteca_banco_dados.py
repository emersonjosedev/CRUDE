import mysql.connector


def criar(conexao, tabela, v1, v2=False, v3=False, v4=False):
    cursor = conexao.cursor()
    if tabela == "3":
        comando_sql = cursor.execute(f"""INSERT INTO setores (nome) VALUES ('{v1}')""")

    elif tabela == "2":
        comando_sql = (
            f"""INSERT INTO funcionarios (nome,salario) VALUES ('{v1}',{v2})"""
        )

    else:
        comando_sql = (
            f"""INSERT INTO produtos (nome,validade,preco) VALUES ('{v1}',{v2},{v3})"""
        )
    cursor.execute(comando_sql)
    conexao.commit()


def ler(conexao, leia):
    cursor = conexao.cursor()
    cursor.execute(f"SELECT * FROM {leia} ")
    resultados = cursor.fetchall()

    for linha in resultados:
        print(linha)



def deletar(conexao, tabela, id):
    cursor = conexao.cursor()
    cursor.execute(f"DELETE FROM {tabela} WHERE id_{tabela} = {id}")
    conexao.commit()

def atualizar(conexao, tabela, id, coluna, novo_valor):
    cursor = conexao.cursor()
    cursor.execute(f"UPDATE {tabela} SET {coluna} = %s WHERE id_{tabela} = %s", (novo_valor, id))
    conexao.commit()
