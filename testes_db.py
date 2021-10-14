import sqlite3


con = sqlite3.connect("./db/db.db")

DBcursor = con.cursor()

# Linha abaixo usada para criar tabela no db de "USUARIOS" com colunas "nome" e "senha"
# Após usada uma vez, não será mais usada
# DBcursor.execute("CREATE TABLE USUARIOS (nome, senha)")

# Linha abaixo irá criar previamente os usuários
# DBcursor.execute("INSERT INTO USUARIOS (nome, senha) VALUES ('Rafael', '123456')")
# con.commit()

# Teste de busca de senha
query = DBcursor.execute("SELECT senha FROM USUARIOS WHERE senha = '0'").fetchall()
print(query)
print(len(query))