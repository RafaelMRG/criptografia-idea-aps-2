# Importei a biblioteca na pasta /bibliotecas/biblio.py nomeando a para lib
import bibliotecas.biblio as lib

# Guardei o return da função da biblioteca na variavel teste
# Como a biblioteca foi renomeada para lib na hora de importar podemos chama-la com o prefixo lib. apenas
teste = lib.biblioteca_print()


# Printei o retorno da função da biblioteca
print(teste)
