def biblioteca_print():
    linhaSeparadora = "*" * 30
    return f"\n{linhaSeparadora}\nControle de acesso a embarcação\n{linhaSeparadora}\n"
# os \n acima serve para pular uma linha no terminal

# Vamos usar a função abaixo para pedir o usuário para inserir sua senha
def userInput(mensagem):
    return str(input(mensagem))

# As duas funções de check abaixo usam o retorno da chamada no DB (retornam os dados em tuplas, ex: se a chamada achar uma senha igual, retorna a senha como string dentro de uma tupla, caso não ache nada, retorna uma tupla vazia, por isso fazemos a checagem do length da tupla)
def checkSenha(senha):
    if (len(senha)) > 0:
        return True
    else:
        return False

def checkNome(nome):
    if (len(nome) > 0):
        return True
    else:
        return False

def checkChave(chave):
    if (len(chave) > 0):
        return True
    else:
        return False

def msgComandoErro():
    print("\n=== Comando errado ou indisponível ===\n")

def msgListarCmds():
    print("\nPara listar os comandos novamente, execute o comando 1")

def msgLixoRemovido():
    ("\nLixo removido do banco de dados com sucesso\n")

def msgLixoInserido():
    print("\nLixo inserido no banco de dados com sucesso\n")

def msgListaCmds():
    print(f"\n=== Lista de comandos ===\n")
    print("1 - Listar comandos")
    print("2 - Listar lixos")
    print("3 - Listar usuários com acesso")
    print("4 - Inserir lixo no banco de dados")
    print("5 - Remover lixo no banco de dados")
    print("9 - Sair do programa")

def msgUserErro():
    print("\n\n-------\nNome de usuário incorreto\n-------\n\n")

def msgSenhaErro():
    print("\n\n-------\nDados de login incorretos, tente novamente\n-------\n\n")

def msgSenhaErro2():
    print("\n\nSenha possuí menos que 3 caracteres\n\n")

def msgLoginOk(user):
    mensagem = f"\nUsuário {user} logado com sucesso"
    print(mensagem)
    print(len(mensagem) * "-")
    print(len(mensagem) * "-" + "\n")

def msgSeparador():
    print("\n" + "-" * 40)


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

# Versão 1.0
# - Criação inicial da biblioteca

# Versão 1.1
# - Adicionado funções de verificação de senha e email

# Versão 1.2
# - Adicionado funções de verificação de chave de criptografia

# Versão 1.3
# - Adicionado funções de mensagens

# Versão 1.4
# - Adicionado versão nova de criptografia que aceita mais de 8 caracteres

# Versão 1.5
# - Modificado o print de retorno para o programa principal, transformando o print em um cabeçalho de programa com título