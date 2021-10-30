# Imports utilizado por arquivo
# /main.py => bibliotecas.biblio, bibliotecas.funcoes_db
# /teste_db.py => sqlite3
# /funcoes_db.py => sqlite3
# /testes_extras.py => binascii, os

from bibliotecas.funcoes_db import queryChave
from bibliotecas.biblio import *
import bibliotecas.funcoes_db as dbf
from bibliotecas.IDEA import IDEA


def main():


	# Print da versão da biblioteca e confirmação que a biblioteca foi importada corretamente
	print(biblioteca_print())


	# Salvando a mensagem mostrada para o usuário na hora de pedir os dados de login
	msgInsiraSuaSenha = "Insira sua senha abaixo: \n"
	msgInsiraSeuUsuario = "Insira seu nome de usuário abaixo: \n"

	while True:

		# Input do usuário
		user = userInput(msgInsiraSeuUsuario)
		print("") # Print para adicionar linha em branco entre os inputs (design)
		
		# Laço que so quebra se senha for menor que 8 caracteres
		while True:
		# Salvando a senha na variável senha com o input do usuário voltando como string (função da biblioteca)
		# Input da senha
			senha = userInput(msgInsiraSuaSenha)
			if (len(senha) < 3):
				msgSenhaErro2()
			else:
				break

		# Este laço abaixo encripta a senha caso o usuário exista e executa uma função de checagem contra os dados do DB que retornam false ou true
		if (len(queryChave(user)) > 0):
			
			
			chave = int(queryChave(user)[0][0])
			idea = IDEA(chave)
			
			senha_split = process_input(senha)
			
			for i in range(len(senha_split)):
				senha_split[i] = idea.encrypt(senha_split[i])
			
			# As funções abaixo (biblio.py) retorna true se os dados inseridos existem no DB, se não, retornam false
			dbSenha = checkSenha(dbf.querySenha(senha_split))
			dbNome = checkNome(dbf.queryUsuario(user))
			
			# Caso os dados do DB sejam iguais aos dados inputados pelo usuário iniciaremos uma sessão de usuário, caso estejam incorretos iremos finalizar o programa
			if (dbSenha == True and dbNome == True):
				logado = True
				msgLoginOk(user)
				break
			else:
				msgSenhaErro()
				logado = False
		else:
			msgUserErro()
			logado = False



	# A partir deste ponto, qualquer função que precisa ser chamada logado, iremos sempre verificar se logado = True

	if logado:
		
		# Comandos

		def listar_comandos():
			msgListaCmds()
		
		def listar_lixo():
			msgSeparador()
			listaLixo = dbf.queryLixo()
			print(f"\n\nLegenda RISCO: 3 níveis, 3 = mais perigoso, 1 = menos perigoso\n")
			print(f"Material{' ' * (25 - int(len('Material')))}Peso{' ' * (5 - int(len('Peso')))}Risco\n")
			for i in listaLixo:
				espaço1 = (25 - int(len(i[0]))) * " "
				espaço2 = (5 - int(len(i[1]))) * " "
				print(f"{i[0]}{espaço1}{i[1]}kg{espaço2}{i[2]}")
		
		def listar_usuarios():
			msgSeparador()
			listaUsers = dbf.queryUsers()
			print("\nUsuários\n")
			for i in listaUsers:
				print(i[0])
    
		def criar_lixo():
			msgSeparador()
			lixoNome = str(input("\nInsira o nome do material radioativo: "))
			
			while True:
				try:
					lixoPeso = str(int(input("Insira o peso do material radioativo(número): ")))
				except:
					print("Entrada incorreta, tente novamente")
				else:
					break
			
			while True:
				try:
					lixoRisco = str(int(input("Insira o risco do material radioativo(número): ")))
				except:
					print("Entrada incorreta, tente novamente")
				else:
					break
			
			queryCompleta = dbf.queryInsertLixo(lixoNome, lixoPeso, lixoRisco)
			if queryCompleta == True:
				msgLixoInserido()
    
		def remover_lixo():
			msgSeparador()
			lixoNome = str(input("\nInsira o nome do material radioativo que deseja remover: "))
			queryCompleta = dbf.queryRemoveLixo(lixoNome)
			if queryCompleta == True:
				msgLixoRemovido()
		
		# Fim comandos
		
		listar_comandos()
		
		# Permite o usuário executar comandos sem sair do programa
		while True:
			# Imprime a lista de comandos possiveis
			msgListarCmds()
			
			try:
				comando_do_usuario = int(input("\n\n Insira um dos comandos (numero):"))
			except:
				msgComandoErro()
			else:
				if comando_do_usuario == 1:
					listar_comandos()
				if comando_do_usuario == 2:
					listar_lixo()
				if comando_do_usuario == 3:
					listar_usuarios()
				if comando_do_usuario == 4:
					criar_lixo()
				if comando_do_usuario == 5:
					remover_lixo()
				if comando_do_usuario == 9:
					break


	print("\n\nPROGRAMA FECHADO COM SUCESSO\n")
	# Fecha conexão com o DB


# Se o arquivo que está sendo executado for este, ele irá rodar todo código acima, caso seja usado como um import, o código não será executado
if __name__ == '__main__':
    main()