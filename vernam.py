#Autor: Jean Carlos Martins Miguel
#Disciplina: Segurança de Redes
#Universidade Tecnológica Federal do Paraná
#github: jeanmmiguel


import sys

import random

import string
from typing_extensions import LiteralString



vetor_alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
vetor_index = '' #guarda pos do index texto2 == chave

def decifrar_mensagem(texto,texto2):
    texto_gravar = ""
    
    index_chave = 0
    pos = 0

    for aux in texto:
            aux_index = vetor_alfabeto.find(aux)
            index_chave = vetor_alfabeto.find(texto2[0])
            if aux_index != -1:
                palavra_letra = aux_index - index_chave
                palavra_letra= palavra_letra % len(vetor_alfabeto)
                texto_gravar += vetor_alfabeto[palavra_letra]

            else:
                texto_gravar += aux
            pos = pos + 1       
    return print(texto_gravar)



def cifrar_mensagem(texto,texto2):
    texto_gravar = ""
    
    index_chave = 0
    pos = 0

    for aux in texto:
            aux_index = vetor_alfabeto.find(aux)
            index_chave = vetor_alfabeto.find(texto2[0])
            if aux_index != -1:
                palavra_letra = aux_index + index_chave
                if palavra_letra >= 0:
                    palavra_letra = palavra_letra % len(vetor_alfabeto)
                else:
                    palavra_letra = palavra_letra + len(vetor_alfabeto)
                    palavra_letra = palavra_letra % len(vetor_alfabeto)
                texto_gravar += vetor_alfabeto[palavra_letra]
            else:
                texto_gravar += aux
            pos = pos + 1       
    return print(texto_gravar)

    
arquivo = open(sys.argv[2], "r", encoding='utf-8') # Abrir o arquivo passado por argumento como leitura
texto = arquivo.read() # fazer leitura do arquivo e guardar na variavel texto
arquivo.close()

tamanho = len(texto)
guardar_chave = ''
number_of_strings = 1
length_of_string = tamanho





if sys.argv[1] == "c":
    for x in range(number_of_strings):   
        guardar_chave += (''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string+10)))
        key_file  = open("key.txt","w")
        key_file.write(guardar_chave)
    cifrar_mensagem(texto,guardar_chave)

if sys.argv[1] == "d":

    arquivo = open("key.txt", "r", encoding='utf-8') 
    texto2 = arquivo.read()
    arquivo.close()
    decifrar_mensagem(texto,texto2)