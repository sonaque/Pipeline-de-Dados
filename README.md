📊 Pipeline de Dados – Vendas e Operações
📌 Visão Geral
Este projeto implementa um pipeline de dados end-to-end para simular o cenário de uma empresa de e-commerce que precisa centralizar, tratar e disponibilizar informações de vendas e operações.

O objetivo é demonstrar competências em engenharia de dados e programação, cobrindo desde a ingestão até o consumo dos dados via API e dashboards.

🎯 Objetivos do Projeto
Centralizar dados de múltiplas fontes criadas(CSV).

Tratar inconsistências e aplicar regras de negócio.

Modelar banco de dados relacional para análise.

Criar dashboard interativo (Power BI).

Automatizar e organizar o fluxo (Docker).

🧠 Problema de Negócio (Fictício)
A empresa vende produtos online, mas os dados chegam de fontes diferentes, com erros e sem padronização.
O time precisa de dados confiáveis para calcular métricas como receita, ticket médio e recorrência de clientes.

🏗️ Arquitetura da Solução
mermaid
flowchart LR
    A[Fontes de Dados] --> B[Extract - Python]
    B --> C[Transform - Python]
    C --> D[Load]
    D --> F[BI - Power BI]
📦 Fontes de Dados
Vendas (CSV): data, produto, produto id, quantidade, valor, status, cliente id, cliente nome

Produtos (CSV): id, nome, categoria, preço base, custo

Clientes (CSV): id, nome, cidade, estado, data de cadastro

👉 Dados propositalmente sujos para simular cenários reais.

🧪 Regras de Negócio (Apicadas propositalmente no Power Query)
Receita = quantidade × valor

Ticket médio por cliente

Receita por estado

📂 Estrutura do Projeto
Código
Pipeline-de-Dados/
├── data/
│   ├── raw/          # Dados brutos
│   ├── processed/    # Dados tratados
├── etl/
│   ├── extract.py    # Extração
│   ├── transform.py  # Transformação
│   ├── load.py       # Carga no banco
├── dashboard/
│   └── powerbi.pbix  # Dashboard Power BI
├── logs/             # Logs de execução
├── docker-compose.yml (opcional)
├── requirements.txt  # Dependências Python
├── README.md
⚙️ Requisitos
Python 3.10+

🚀 Instalação e Execução
bash
# Clonar repositório
git clone https://github.com/seuusuario/pipeline-dados-empresa.git
cd Pipeline-de-Dados

# Instalar dependências
pip install -r requirements.txt

# Executar ETL
python etl/extract.py
python etl/transform.py
python etl/load.py

# Subir API
uvicorn api.main:app --reload
📊 Exemplos de Consumo da API
Receita total: GET /receita

Receita por período: GET /receita?start=2024-01-01&end=2024-01-31

Top produtos: GET /top-produtos

📈 Dashboard (Power BI)
O dashboard conecta diretamente ao banco de dados e apresenta:

Receita total e por estado

Ticket médio por cliente

Top produtos vendidos

Classificação de clientes (novo vs recorrente)
