
import sys

#python3 analisador.py analisar.txt
total_frequencia = {}
total = 0

arquivo = open(sys.argv[1], "r") # Abrir o arquivo passado por argumento como leitura
texto = arquivo.read() # fazer leitura do arquivo e guardar na variavel texto
arquivo.close()

#def analisar_Frequencia(texto):

for letra in texto:
    if letra.isalpha() or letra.isdigit(): #verifica se é alfabeto
        if letra not in total_frequencia:
            total_frequencia[letra] = 1
        else:
            total_frequencia[letra] += 1
            total += 1

print(total)

for i in total_frequencia:
    total_frequencia[i] /= total

print(total_frequencia)



