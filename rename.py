import os
# O Script renomeia todos os arquivos de um diretório
# O diretório deve ser informado na variável DIR.
# O exemplo acrescenta um indice numérico ao nome do arquivo.
id = 0
DIR = "./instancias_moldes/1-10/J=20 M=4 1，10/"
os.chdir(DIR)
for filename in os.listdir("."):
    id = id + 1
    os.rename(filename, str(id) + "_" + filename)