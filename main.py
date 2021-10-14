# Imports utilizado por arquivo
# /main.py => bibliotecas.biblio, bibliotecas.funcoes_db
# /teste_db.py => sqlite3
# /funcoes_db.py => sqlite3
# /testes_extras.py => binascii, os

from bibliotecas.funcoes_db import queryChave


def main():
	# Importei a biblioteca na pasta /bibliotecas/biblio.py nomeando a para lib
	from bibliotecas.biblio import checkSenha, checkNome, userInput, biblioteca_print as biblioversion
	import bibliotecas.funcoes_db as dbf
	from bibliotecas.IDEA import IDEA


	# Print da versão da biblioteca e confirmação que a biblioteca foi importada corretamente
	print(biblioversion())


	# Salvando a mensagem mostrada para o usuário na hora de pedir os dados de login
	msgInsiraSuaSenha = "Insira sua senha abaixo: \n"
	msgInsiraSeuUsuario = "Insira seu nome de usuário abaixo: \n"

	while True:
		# Salvando a senha na variável senha com o input do usuário voltando como string (função da biblioteca)

		# Input do usuário
		user = userInput(msgInsiraSeuUsuario)
		print("") # Print para adicionar linha em branco entre os inputs (design)
		
		# Input da senha
		# Laço que so quebra se senha for menor que 8 caracteres
		while True:
			senha = userInput(msgInsiraSuaSenha)
			if (len(senha) > 8):
				print("\n\nSenha possuí mais que 8 caracteres\n\n")
			else:
				break

		# Este laço abaixo encripta a senha caso o usuário exista e executa uma função de checagem contra os dados do DB que retornam false ou true
		if (len(queryChave(user)) > 0):
			
			chave = int(queryChave(user)[0][0])
			idea = IDEA(chave)
			
			senhaHex = int(senha.encode("utf-8").hex().upper(), 16)
			senhaCript = idea.encrypt(senhaHex)

			# As funções abaixo (biblio.py) retorna true se os dados inseridos existem no DB, se não, retornam false
			dbSenha = checkSenha(dbf.querySenha(senhaCript))
			dbNome = checkNome(dbf.queryUsuario(user))
			
			# Caso os dados do DB sejam iguais aos dados inputados pelo usuário iniciaremos uma sessão de usuário, caso estejam incorretos iremos finalizar o programa
			if (dbSenha == True and dbNome == True):
				logado = True
				mensagem = f"\nUsuário {user} logado com sucesso"
				print(mensagem)
				print(len(mensagem) * "-" + "\n")
				break
			else:
				print("\n\n---\nDados de usuário incorreto, tente novamente\n---\n\n")
				logado = False
		else:
			print("\n\n---\nNome de usuário incorreto\n---\n\n")



	# A partir deste ponto, qualquer função que precisa ser chamada logado, iremos sempre verificar se logado = True

	if logado:
		
		# Comandos

		def listar_comandos():
			print(f"\nLista de comandos:\n")
			print("1 - Listar comandos")
			print("2 - Listar lixos")
			print("3 - Listar usuários com acesso")
			print("4 - Inserir lixo no banco de dados")
			print("5 - Remover lixo no banco de dados")
			print("9 - Sair do programa")
		
		def listar_lixo():
			listaLixo = dbf.queryLixo()
			print(f"\n\nLegenda RISCO: 3 níveis, 3 = mais perigoso, 1 = menos perigoso\n")
			print(f"Material{' ' * (25 - int(len('Material')))}Peso{' ' * (5 - int(len('Peso')))}Risco\n")
			for i in listaLixo:
				espaço1 = (25 - int(len(i[0]))) * " "
				espaço2 = (5 - int(len(i[1]))) * " "
				print(f"{i[0]}{espaço1}{i[1]}kg{espaço2}{i[2]}")
			
		
		def listar_usuarios():
			listaUsers = dbf.queryUsers()
			print("\nUsuários\n")
			for i in listaUsers:
				print(i[0])
    
		def criar_lixo():
			lixoNome = str(input("\nInsira o nome do material radioativo: "))
			lixoPeso = str(input("Insira o peso do material radioativo(número): "))
			lixoRisco = str(input("Insira o risco do material radioativo(número): "))
			queryCompleta = dbf.queryInsertLixo(lixoNome, lixoPeso, lixoRisco)
			if queryCompleta == True:
				print("\nLixo inserido no banco de dados com sucesso\n")
    
		def remover_lixo():
			lixoNome = str(input("\nInsira o nome do material radioativo que deseja remover: "))
			queryCompleta = dbf.queryRemoveLixo(lixoNome)
			if queryCompleta == True:
				print("\nLixo removido do banco de dados com sucesso\n")
		
		# Fim comandos
		
		
		# Permite o usuário executar comandos sem sair do programa
		while True:
			# Imprime a lista de comandos possiveis
			listar_comandos()
			
			comando_do_usuario = int(input("\n\n Insira um dos comandos (numero):"))
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


	# Fecha conexão com o DB
	dbf.queryClose()


# Se o arquivo que está sendo executado for este, ele irá rodar todo código acima, caso seja usado como um import, o código não será executado
if __name__ == '__main__':
    main()