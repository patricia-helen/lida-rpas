#!/bin/bash

echo "Iniciando configuração do ambiente..."

# Define o diretório do projeto como diretório de trabalho
cd "$(dirname "$0")"

# Criação do ambiente virtual
echo "Criando ambiente virtual..."
python3 -m venv venv
echo "Ambiente virtual criado."

# Ativação do ambiente virtual existente
echo "Ativando o ambiente virtual..."
source ~/lida-rpas/bin/activate
echo "Ambiente virtual ativado."

# Atualização do pip
echo "Atualizando pip..."
pip install --upgrade pip

# Instalação das dependências a partir do requirements.txt
echo "Instalando dependências..."
pip install -r requirements.txt
echo "Dependências instaladas."

# Execução de outras configurações necessárias
# Por exemplo, migrações e coleta de arquivos estáticos
echo "Aplicando migrações..."
python manage.py migrate

echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput  # O flag --noinput evita que perguntas sejam feitas

echo "Configuração concluída."

