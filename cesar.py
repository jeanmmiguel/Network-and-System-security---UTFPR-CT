#Autor: Jean Carlos Martins Miguel
#Disciplina: Segurança de Redes
#Universidade Tecnológica Federal do Paraná
#github: jeanmmiguel


#python3 cesar.py d 5 decifrar.txt > teste1

import sys
vetor_alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"


def decifrar_mensagem(chave,texto):
        texto_gravar = ''
    
        for aux in texto:
                indice_texto = vetor_alfabeto.find(aux)
                                 
                if indice_texto != -1:
                      alterar_letra = indice_texto - chave
                      alterar_letra = alterar_letra % len(vetor_alfabeto)
                      texto_gravar += vetor_alfabeto[alterar_letra]
                else:
                         texto_gravar+= aux   

        return print(texto_gravar)



def cifrar_mensagem(chave,texto):
        texto_gravar = ''


        for aux in texto:
                indice_texto = vetor_alfabeto.find(aux)
                if indice_texto == -1:
                        texto_gravar += aux
                else:
                        alterar_letra =  indice_texto + chave
                        alterar_letra = alterar_letra % len(vetor_alfabeto)
                        texto_gravar += vetor_alfabeto[alterar_letra]

        return print(texto_gravar)


arquivo = open(sys.argv[3], "r") # Abrir o arquivo passado por argumento como leitura
texto = arquivo.read() # fazer leitura do arquivo e guardar na variavel texto
arquivo.close()


chave = int(sys.argv[2])
if sys.argv[1]== "c" or sys.argv[1] == "C":
         cifrar_mensagem(chave,texto)
if sys.argv[1] == "d" or sys.argv[1] == "D":
         decifrar_mensagem(chave,texto)