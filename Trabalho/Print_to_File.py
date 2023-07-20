# ---------------------------------------------------------------------------------------------------
# Lê os nomes dos arquivos que estão na pasta de origem passada por parâmetro e retorna,
# caso exista, a próxima sequência numérica válida com base no nome do arquivo.
# 
# Exemplo: Se forem encontrados os arquivos 'a1.txt' e 'a2.txt', o programa retornará 3, que é
#          a próxima sequência que pode ser utilizada para criar o arquivo 'a3.txt'.
# ---------------------------------------------------------------------------------------------------
import os
import sys
import pyscreenshot
import subprocess


def pyshot():
    # part of the screen
    im = pyscreenshot.grab(bbox=(42, 322, 973, 846))  # X1,Y1,X2,Y2
    # save image file
    im.save("UltimaCaptura.png")

def extrair_seq(nome_arquivo):
    """
    Extrai uma sequência numérica do nome de um arquivo. Se existirem duas ou mais sequências, só extrairá a que estiver mais no final do nome
    do arquivo. Se não existir uma sequência, retorna -1.
    """
    nome_arq_sem_extensao = nome_arquivo.split(".")[0]
    seq = ""

    # Obtêm a sequência de trás para frente, pois começa a ler do último caracter do nome do arquivo
    for i in range(len(nome_arq_sem_extensao)-1, -1, -1):
        if nome_arq_sem_extensao[i].isdigit():
            seq += nome_arq_sem_extensao[i]
        else:
            break
    
    if seq != "":
        return int(seq[::-1]) # Desinverte a sequência
    else:
        return -1

# #!/bin/bash

# inicial_arquivo="BD"

# pasta_origem=$(pwd)

# pasta_destino="/home/gabriel_aquino/Documentos/workspace/Estacio_Materia_Banco_de_Dados/img3/"

# proxima_seq=$(python3.8 proxima_seq.py $pasta_destino)

# # Verifica se retornou uma sequência inteira positiva e cria o arquivo
# if [[ $proxima_seq =~ ^[0-9]+$ ]]; then
#    if [ $proxima_seq -gt -1 ]; then
#        #echo "Novo arquivo criado: "$pasta_destino/$inicial_arquivo$proxima_seq
#        mv $pasta_origem/UltimaCaptura.png $pasta_destino/$inicial_arquivo$proxima_seq.png # inserir o MV aqui
#    fi
# else
#    echo "ERRO: "$proxima_seq >&2; exit 1 
# fi


if __name__ == "__main__":
    # pyshot()



    pasta_destino = ""

    if len(sys.argv) > 1:
        pasta_destino = sys.argv[1]
    else:
        print(f"\nInforme o nome da pasta onde estão os arquivos como parâmetro na chamada do programa '{sys.argv[0]}'!\n")
        exit(1)


    try:
        arqs = os.listdir(pasta_destino)
    except FileNotFoundError:
        print(f"\nA pasta '{pasta_destino}' não existe!\n")
        exit(1)

    maior_sequencia = -2

    for a in arqs:
        if not os.path.isdir(os.path.join(pasta_destino, a)):
            seq = extrair_seq(a)
            if seq > maior_sequencia:
                maior_sequencia = seq
    
    print(maior_sequencia + 1)


