def biblioteca_print():
    return "\n\nBiblioteca versão: 1.2\nRetorno completo\n\n"
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




# Versão 1.0
# - Criação inicial da biblioteca

# Versão 1.1
# - Adicionado funções de verificação de senha e email

# Versão 1.2
# - Adicionado funções de verificação de chave de criptografia