#!/bin/bash


$print

inicial_arquivo="BD"

pasta_origem=$(pwd)

print=$(python3.8 $pasta_origem/pyshot.py)

pasta_destino="/home/gabriel_aquino/Documentos/github/workspace/_Disciplinas/Estacio_Materia_Banco_de_Dados/img3/"

clipboardini="![](img3/$inicial_arquivo"
clipboardfin=".png)"

proxima_seq=$(python3.8 $pasta_origem/proxima_seq.py $pasta_destino)

# Verifica se retornou uma sequência inteira positiva e cria o arquivo
if [[ $proxima_seq =~ ^[0-9]+$ ]]; then
   if [ $proxima_seq -gt -1 ]; then
       #echo "Novo arquivo criado: "$pasta_destino/$inicial_arquivo$proxima_seq
       mv $pasta_origem/UltimaCaptura.png $pasta_destino/$inicial_arquivo$proxima_seq.png
      #  $pasta_destino/$inicial_arquivo$proxima_seq.png | xclip       
   fi
else
   echo "ERRO: "$proxima_seq >&2; exit 1 
fi 

echo $clipboardini$proxima_seq$clipboardfin | xclip -selection clipboard

sleep 0.1







