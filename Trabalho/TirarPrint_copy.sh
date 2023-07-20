#! /usr/bin/bash
# #Iniciando Print
dirini=/home/gabriel_aquino/Imagens
#dirfin=
arquivos=$(ls -1 $dir | grep .png | cut -d. -f1)
ultimo=$(find $dirini -type f -maxdepth 1 -printf "%C@ %p\\n" | sort -r | awk 'NR==1 {print $2}')
echo $dirini
echo $arquivos
echo $ultimo
