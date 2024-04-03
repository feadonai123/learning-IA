#!/bin/bash

# Número de repetições
N=9

# Loop for para repetir os comandos
for ((i=0; i<=$N; i++)); do
  python graficoAG.py teste_$i.txt &
done