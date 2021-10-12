# Importei a biblioteca na pasta /bibliotecas/biblio.py nomeando a para lib
from bibliotecas.biblio import userInput as userInput, biblioteca_print as biblioversion



# Print da versão da biblioteca e confirmação que a biblioteca foi importada corretamente
print(biblioversion())


# Salvando a mensagem mostrada para o usuário na hora de pedir o input da senha
msgInsiraSuaSenha = "Insira sua senha abaixo: \n"

# Salvando a senha na variável senha com o input do usuário voltando como string (função da biblioteca)
senha = userInput(msgInsiraSuaSenha)

# Salvando o comprimento da senha para multiplicar o tamanho da senha pelo caracter * e "confirmar"	que a senha foi inserida
comprimentoSenha = int(len(senha))

# Confirmação que a senha foi inserida como explicado no comentário anterior
print(f"\nSua senha é:{comprimentoSenha * '*'}\n")