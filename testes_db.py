import sqlite3


con = sqlite3.connect("./bibliotecas/db/banco.db")

DBcursor = con.cursor()


# Linha abaixo usada para criar tabela no db de "usuarios" com colunas "nome", "senha" e chave
# Tabela "lixo"
# e comando para deletar tabela "usuarios"
# Após usada uma vez, não será mais usada

# DBcursor.execute("DROP TABLE usuarios")
# DBcursor.execute("CREATE TABLE usuarios (nome, senha, chave)")
# DBcursor.execute("CREATE TABLE lixo (lixo, peso, risco)")



# Linhas abaixo irá criar previamente os usuários e lista de resíduos radioativos, chaves foram criadas a partir do testes_extras.py e senhas geradas a partir do main.py
# Precisam ser executadas apenas 1 vez

# DBcursor.execute("INSERT INTO usuarios (nome, senha, chave) VALUES ('Rafael', '6316554473449217439', '2860810080134405214')")
# DBcursor.execute("INSERT INTO usuarios (nome, senha, chave) VALUES ('Vivian', '10259176932281485866', '17085172137098893768')")
# DBcursor.execute("INSERT INTO usuarios (nome, senha, chave) VALUES ('Fabio', '5762451042398323849', '11358383868298978893')")
# DBcursor.execute("INSERT INTO usuarios (nome, senha, chave) VALUES ('Fernando', '5217784806661896863', '14713001563363140955')")
# DBcursor.execute("INSERT INTO usuarios (nome, senha, chave) VALUES ('Vinicius', '17299228804581155343', '7693246748904938083')")
# DBcursor.execute("INSERT INTO usuarios (nome, senha, chave) VALUES ('Igor', '13974521050565597877', '15338590261167174220')")
# DBcursor.execute("INSERT INTO usuarios (nome, senha, chave) VALUES ('Lucas', '15187029488001368154', '7622660824036823917')")

# DBcursor.execute("INSERT INTO lixo (lixo, peso, risco) VALUES ('Uranio', '1', '2')")
# DBcursor.execute("INSERT INTO lixo (lixo, peso, risco) VALUES ('Cesio', '2', '2')")
# DBcursor.execute("INSERT INTO lixo (lixo, peso, risco) VALUES ('Plutonio', '5', '3')")
# DBcursor.execute("INSERT INTO lixo (lixo, peso, risco) VALUES ('Yellow Cake', '20', '1')")



# Teste de busca de senha
# query = DBcursor.execute("SELECT senha FROM usuarios WHERE senha = '0'").fetchall()
# print(query)
# print(len(query))





# Finaliza conexão com banco de dados
con.commit()
con.close()