import sqlite3

#con = sqlite3.connect("./bibliotecas/db/banco.db") # inicia a conexão com o DB
#DBcursor = con.cursor() # o cursor é usado para executar comandos no DB


# Função para buscar a coluna senha no DB e retorna uma tupla com a senha caso a senha passada no parametro seja igual a senha do DB
def querySenha(senha):
	try:
		con = sqlite3.connect("./bibliotecas/db/banco.db")
		DBcursor = con.cursor()
		resultado = DBcursor.execute(f"SELECT senha FROM usuarios WHERE senha = '{senha}'").fetchall()
		con.close()
		return resultado
	except:
		print("Houve um erro inesperado no banco de dados")

# Função para buscar a coluna nome no DB e retorna uma tupla com o nome caso o nome passada no parametro seja igual o nome do DB
def queryUsuario(user):
	try:
		con = sqlite3.connect("./bibliotecas/db/banco.db")
		DBcursor = con.cursor()
		resultado = DBcursor.execute(f"SELECT nome FROM usuarios WHERE nome = '{user}'").fetchall()
		con.close()
		return resultado
	except:
		print("Houve um erro inesperado no banco de dados")

# Função para buscar a coluna chave no DB e retorna uma tupla com a chave caso a chave passada no parametro seja igual a chave do DB
def queryChave(user):
	try:
		con = sqlite3.connect("./bibliotecas/db/banco.db")
		DBcursor = con.cursor()
		resultado = DBcursor.execute(f"SELECT chave FROM usuarios WHERE nome = '{user}'").fetchall()
		con.close()
		return resultado
	except:
		print("Houve um erro inesperado no banco de dados")

# Função que termina a conexão com o DB
def queryClose():
	return con.close()

def queryLixo():
	try:
		con = sqlite3.connect("./bibliotecas/db/banco.db")
		DBcursor = con.cursor()
		resultado = DBcursor.execute(f"SELECT * FROM lixo ORDER BY risco ASC").fetchall()
		con.close()
		return resultado
	except:
		print("Houve um erro inesperado no banco de dados")


def queryUsers():
	try:
		con = sqlite3.connect("./bibliotecas/db/banco.db")
		DBcursor = con.cursor()
		resultado =  DBcursor.execute(f"SELECT nome FROM usuarios").fetchall()
		con.close()
		return resultado
	except:
		print("Houve um erro inesperado no banco de dados")

def queryInsertLixo(lixoNome, lixoPeso, lixoRisco):
	try:
		con = sqlite3.connect("./bibliotecas/db/banco.db")
		DBcursor = con.cursor()
		DBcursor.execute(f"INSERT INTO lixo (lixo, peso, risco) VALUES ('{lixoNome}', '{lixoPeso}', '{lixoRisco}')")
		# Faz as mudanças tomarem efeito imediato
		con.commit()
		con.close()
	except:
		print("Houve um erro inesperado no banco de dados")
	return True

def queryRemoveLixo(lixoNome):
	try:
		con = sqlite3.connect("./bibliotecas/db/banco.db")
		DBcursor = con.cursor()
		DBcursor.execute(f"DELETE FROM lixo WHERE lixo='{lixoNome}'")
		con.commit()
		con.close()
		return True
	except:
		print("Houve um erro inesperado no banco de dados")