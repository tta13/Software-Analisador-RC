#!/bin/sh
set -e

echo "Gerando a build da imagem: software-analisador-backend..."
docker build -t software-analisador/backend ./backend

echo "Geração da imagem finalizada."
