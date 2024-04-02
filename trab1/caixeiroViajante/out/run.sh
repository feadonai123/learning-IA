#!/bin/bash

# Número de repetições
N=9

# Loop for para repetir os comandos
for ((i=0; i<=$N; i++)); do
  python graficoAG.py data2/teste9/teste_$i.txt &
done