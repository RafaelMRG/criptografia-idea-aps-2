import binascii
import os

# Criador de key
# Criação de key para 7 usuários(integrantes do grupo)

chaves = []

for i in range(7):
	key = int(binascii.b2a_hex(os.urandom(8)).decode("utf-8"), 16)
	chaves.append(key)

# Chaves geradas

# 2860810080134405214
# 17085172137098893768
# 11358383868298978893
# 14713001563363140955
# 7693246748904938083
# 15338590261167174220
# 7622660824036823917
