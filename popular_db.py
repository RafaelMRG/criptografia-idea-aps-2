import binascii
import os
import sqlite3
from bibliotecas.IDEA import IDEA


con = sqlite3.connect("./bibliotecas/db/banco.db")
DBcursor = con.cursor()

# Este script é destinado para popular o banco de dados com usuários e lista de lixo
# Utilizar este script quando não tiver com um banco de dados completo ou quando quiser
# resetar os dados criptografados

############################################
######## UTILIZAR ESTE SCRIPT APENAS 1 VEZ ########
############################################

# Script para popular banco de dados com nome de usuário, senha e chave de criptografia

# Comandos abaixo deletam tables se existir e cria tables usuarios e lixo


DBcursor.execute("DROP TABLE IF EXISTS lixo")
DBcursor.execute("DROP TABLE IF EXISTS usuarios")
con.commit()
DBcursor.execute("CREATE TABLE usuarios (nome, senha, chave)")
DBcursor.execute("CREATE TABLE lixo (lixo, peso, risco)")
con.commit()


# Processamento de logins
def randomNumber():
    return int(binascii.b2a_hex(os.urandom(8)).decode("utf-8"), 16)

def process_input(seq):
    split = split_characters(seq)
    for i in range(len(split)):
        split[i] = to_hex(split[i])
    return split

def split_characters(seq):
    i = 0
    f = 8
    split_seq = []
    while i < len(seq):
        split_seq.append(seq[i:f])
        i += 8  # Andando de 8 em 8 caracteres
        f += 8
    return split_seq

def to_hex(txt):
    return int(txt.encode("utf-8").hex().upper(), 16)

# Lista de usuário e senha
lista_usuarios = [
    ["Rafael", "teste1"],
    ["Vivian", "223456"],
    ["Fabio", "323456"],
    ["Fernando", "423456"],
    ["Vinicius", "523456"],
    ["Igor", "623456"],
    ["Lucas", "723456"]
]

# Adicionando as keys na lista
for i in lista_usuarios:
	i.append(str(randomNumber()))

# Adicionando senhas processadas na lista
for i in lista_usuarios:
	senha = i[1]
	senha_split = process_input(senha)
	idea = IDEA(int(i[2]))
	for x in range(len(senha_split)):
		senha_split[x] = idea.encrypt(senha_split[x])
	i[1] = (senha_split)

# Populando tabela de usuários
for i in lista_usuarios:
    usuario = i[0]
    senha = i[1]
    key = i[2]
    DBcursor.execute(f"INSERT INTO usuarios (nome, senha, chave) VALUES ('{usuario}', '{senha}', '{key}')")


# Populando lista de lixo
lista_lixo = [
	['Urânio', '1', '2'],
	['Cesio', '2', '2'],
	['Plutonio', '5', '3'],
	['Yellow Cake', '20', '1']
]

for lixo in lista_lixo:
    DBcursor.execute(f"INSERT INTO lixo (lixo, peso, risco) VALUES ('{lixo[0]}', '{lixo[1]}', '{lixo[2]}')")




# Finaliza conexão com banco de dados
con.commit()
con.close()
