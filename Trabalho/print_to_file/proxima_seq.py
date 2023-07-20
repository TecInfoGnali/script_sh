# ---------------------------------------------------------------------------------------------------
# Lê os nomes dos arquivos que estão na pasta de origem passada por parâmetro e retorna,
# caso exista, a próxima sequência numérica válida com base no nome do arquivo.
# 
# Exemplo: Se forem encontrados os arquivos 'a1.txt' e 'a2.txt', o programa retornará 3, que é
#          a próxima sequência que pode ser utilizada para criar o arquivo 'a3.txt'.
# ---------------------------------------------------------------------------------------------------
import os
import sys

#EXTRAI SEQUENCIA
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


if __name__ == "__main__":
    pasta_origem = ""
    qt_digit = 6

    if len(sys.argv) > 1:
        pasta_origem = sys.argv[1]
    else:
        print(f"\nInforme o nome da pasta onde estão os arquivos como parâmetro na chamada do programa '{sys.argv[0]}'!\n")
        exit(1)


    try:
        arqs = os.listdir(pasta_origem)
    except FileNotFoundError:
        print(f"\nA pasta '{pasta_origem}' não existe!\n")
        exit(1)

    maior_sequencia = -2

    for a in arqs:
        if not os.path.isdir(os.path.join(pasta_origem, a)):
            seq = extrair_seq(a)
            if seq > maior_sequencia:
                maior_sequencia = seq

    seq_str = str(maior_sequencia+1)
    maior_sequencia = (qt_digit - len(seq_str)) * "0" + seq_str
    print(maior_sequencia)

