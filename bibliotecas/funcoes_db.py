import sqlite3

con = sqlite3.connect("./bibliotecas/db/banco.db") # inicia a conexão com o DB
DBcursor = con.cursor() # o cursor é usado para executar comandos no DB

# Função para buscar a coluna senha no DB e retorna uma tupla com a senha caso a senha passada no parametro seja igual a senha no DB
def querySenha(senha):
    return DBcursor.execute(f"SELECT senha FROM USUARIOS WHERE senha = '{senha}'").fetchall()

# Função para buscar a coluna nome no DB e retorna uma tupla com o nome caso o nome passada no parametro seja igual o nome no DB
def queryUsuario(user):
    return DBcursor.execute(f"SELECT nome FROM USUARIOS WHERE nome = '{user}'").fetchall()

# Função que termina a conexão com o DB
def queryClose():
    return con.close()