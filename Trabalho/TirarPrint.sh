#! /usr/bin/bash
# #Iniciando Print
pastaOrigem="~/Imagens/"
xdotool mousemove 500 500 click 1;
sleep 1;
xdotool key Shift_L+Print;
sleep 5;
xdotool mousemove 42 322;
sleep 0.2;
xdotool mousedown 1;
sleep 0.1;
xdotool mousemove 973 846;
sleep 0.1;
xdotool mouseup 1;
sleep 1;
xdotool mousemove 500 500 click 1;
sleep 1;
#Renomeando Arquivo em Banco de Dados
xdotool mousemove 2234 1823 click 1 type 'mv ~/Imagens/Cap';
sleep 1;
xdotool key KP_Tab;
sleep 1;
xdotool type '/home/gabriel_aquino/Documentos/workspace/Estacio_Materia_Banco_de_Dados/img3/BD000.png';
sleep 0.1;
xdotool key Left;
sleep 0.1;
xdotool key Left;sleep 0.1;xdotool key Left;sleep 0.1;xdotool key Left