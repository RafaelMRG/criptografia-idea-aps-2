import binascii
import os
from IDEA import IDEA


def encrypt_compare(ecpt1, ecpt2):
    if len(ecpt1) != len(ecpt2):
        return False
    for cod1, cod2, in zip(ecpt1, ecpt2):
        if cod1 != cod2:
            return False
    return True


# Processa sequências com mais de 8 caracteres
def process_input(seq):
    split = split_characters(seq)
    for i in range(len(split)):
        split[i] = to_hex(split[i])
    return split


def to_hex(txt):
    return int(txt.encode("utf-8").hex().upper(), 16)


def split_characters(seq):
    i = 0
    f = 8
    split_seq = []
    while i < len(seq):
        split_seq.append(seq[i:f])
        i += 8  # Andando de 8 em 8 caracteres
        f += 8
    return split_seq


def main():

    # Gera uma chave aleatória
    key = int(binascii.b2a_hex(os.urandom(8)).decode("utf-8"), 16)

    idea = IDEA(key)

    login = "lgmpinto"
    login_split = process_input(login)

    senha = "1234567890"
    senha_split = process_input(senha)

    print("\nCriptografando o login")
    for i in range(len(login_split)):
        login_split[i] = idea.encrypt(login_split[i])

    print("\nCriptografando a senha")
    for i in range(len(senha_split)):
        senha_split[i] = idea.encrypt(senha_split[i])
    print()

    # Esse dicionário de credenciais vai estar salvo em uma tabela do banco de dados
    cred = {
        'l_cript': login_split,
        's_cript': senha_split,
        'key': key
    }

    login = input('Entre com o login: ')
    login_novo_split = process_input(login)
    senha = input('Entre com a senha: ')
    senha_nova_split = process_input(senha)

    idea = IDEA(cred['key'])

    print("\nCriptografando o novo login")
    for i in range(len(login_split)):
        login_novo_split[i] = idea.encrypt(login_novo_split[i])
    print("\nCriptografando a nova senha")
    for i in range(len(senha_split)):
        senha_nova_split[i] = idea.encrypt(senha_nova_split[i])

    if encrypt_compare(cred['l_cript'], login_novo_split):
        if encrypt_compare(cred['s_cript'], senha_nova_split):
            print('\nUsuário reconhecido. Acesso autorizado.')
            return
    print('\nUsuário não reconhecido. Acesso negado.')


if __name__ == '__main__':
    main()