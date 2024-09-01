# LIDA-RPAS: Supervised Classification of Multispectral Images for Land Cover Mapping

Este projeto explora a classificação supervisionada de imagens multiespectrais para mapeamento de cobertura do solo, utilizando técnicas de aprendizado de máquina, como Deep Learning e Máquinas de Vetores de Suporte (SVM). Através do uso do Python, o projeto foca na categorização baseada em pixels para análise de imagens e processamento de dados geoespaciais.

## Visão Geral

O projeto LIDA-RPAS (Laboratório de Inovação, Desenvolvimento e Aplicação de Sistemas de Aeronaves Pilotadas Remotamente) visa aprimorar a detecção e controle de plantas invasoras em plantios florestais. Utilizando RPAS equipados com câmeras multiespectrais, este projeto desenvolve técnicas de classificação supervisionada para mapeamento preciso da cobertura do solo, com um foco particular em:

- **Processamento de Imagens**: Aplicação de técnicas de deep learning e SVM para classificar pixels em categorias específicas.
- **Detecção de Plantas Invasoras**: Uso de algoritmos de aprendizado de máquina para identificar áreas infestadas por plantas invasoras.
- **Análise de Dados Geoespaciais**: Integração de bibliotecas Python como `rasterio`, `numpy`, e `matplotlib` para análise e visualização de dados.

## Processamento da Imagem

### Voo Original
Imagem capturada por um drone durante o voo:

![Voo Original](https://github.com/patricia-helen/lida-rpas/blob/main/Voo_01.png)

### Voo Processado
Imagem processada após uso de modelo

![Voo Processado](https://github.com/patricia-helen/lida-rpas/blob/main/Voo_02.png)

## Como Executar


**Clone o Repositório**:
   
   git clone <URL_DO_REPOSITORIO>
   cd meu_projeto

**Crie um Ambiente Virtual**:

bash

python3 -m venv venv
source venv/bin/activate  # No Windows, use: venv\Scripts\activate

**Instale as Dependências**:

bash

pip install -r requirements.txt

**Execute as Migrações do Banco de Dados**:

bash

python manage.py migrate

**Inicie o Servidor**:

bash

python manage.py runserver

**Acesse a Aplicação**:

Abra o navegador e vá para http://127.0.0.1:8000/.

