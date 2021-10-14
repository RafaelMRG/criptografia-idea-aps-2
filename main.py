# Imports utilizado por arquivo
# /main.py => bibliotecas.biblio, bibliotecas.funcoes_db
# /teste_db.py => sqlite3
# /funcoes_db.py => sqlite3


# Importei a biblioteca na pasta /bibliotecas/biblio.py nomeando a para lib
from bibliotecas.biblio import checkSenha, checkNome, userInput, biblioteca_print as biblioversion
import bibliotecas.funcoes_db as dbf


# Print da versão da biblioteca e confirmação que a biblioteca foi importada corretamente
print(biblioversion())


# Salvando a mensagem mostrada para o usuário na hora de pedir os dados de login
msgInsiraSuaSenha = "Insira sua senha abaixo: \n"
msgInsiraSeuUsuario = "Insira seu nome de usuário abaixo: \n"

# Salvando a senha na variável senha com o input do usuário voltando como string (função da biblioteca)
user = userInput(msgInsiraSeuUsuario)
print("") # Print para adicionar linha em branco entre os inputs (design)
senha = userInput(msgInsiraSuaSenha)





# Salvando o comprimento da senha para multiplicar o tamanho da senha pelo caracter * e "confirmar"	que a senha foi inserida
comprimentoSenha = int(len(senha))

# Confirmação que a senha foi inserida como explicado no comentário anterior
print(f"\nSua senha é:{comprimentoSenha * '*'}")
print(f"\nSeu usuário é:{user}\n")





# As funções abaixo (biblio.py) retorna true se os dados inseridos existem no DB, se não, retornam false
checkSenha = checkSenha(dbf.querySenha(senha))
checkNome = checkNome(dbf.queryUsuario(user))

# A estrutura de seleção abaixo verifica se os dados inputados pelo usuário retornam True tanto para usuário como para senha e caso seja verdadeiro definem a sessão como logada na variável "logado" e imprime uma mensagem de login realizado com sucesso
if (checkSenha == True and checkNome == True):
    logado = True
    mensagem = f"\nUsuário {user} logado com sucesso"
    print(mensagem)
    print(len(mensagem) * "-" + "\n")
else:
    logado = False
    print("Credenciais de login incorretas, tente novamente")

# A partir deste ponto, qualquer função que precisa ser chamada logado, iremos sempre verificar se logado = True




# Fecha conexão com o DB
dbf.queryClose()