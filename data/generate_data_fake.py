import pandas as pd
import random
from faker import Faker 
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"

RAW_DIR.mkdir(parents=True, exist_ok=True)


fake = Faker('pt_BR')


clientes = []

for _ in range(20):
    clientes.append({
        "id": fake.uuid4(),
        "cidade": fake.city(),
        "estado": random.choice(["SP", "São Paulo", "S.P.", "RJ", "Rio de Janeiro"]),
        "data_cadastro": fake.date_between(start_date = "-2y", end_date = "today"),
    })

df_clientes = pd.DataFrame(clientes)
df_clientes.to_csv(RAW_DIR / "clientes.csv", index=False)

produtos = []

produtos_por_categoria = {
    "Alimentos": ["Arroz", "Feijão", "Macarrão", "Leite", "Pão", "Café", "Açúcar", "Óleo de soja", "Carne bovina", "Frango"],
    "Eletrônicos": ["Smartphone", "Notebook", "Televisão", "Fone de ouvido", "Tablet", "Console de videogame", "Impressora", "Monitor", "Caixa de som", "Smartwatch"],
    "Moda": ["Camiseta", "Calça jeans", "Vestido", "Jaqueta", "Tênis", "Sandália", "Bolsa", "Boné", "Saia", "Óculos de sol"]
}


for _ in range(15):
    categoria = random.choice(["Eletrônicos", "Moda", "Alimentos", "Eletronic"])
    
    if categoria in produtos_por_categoria: 
        nome = random.choice(produtos_por_categoria[categoria]) 
    else: 
        nome = random.choice(produtos_por_categoria["Eletrônicos"])

    preco_base = round(random.uniform(50, 2000), 2)
    custo = round(random.uniform(40, preco_base * 0.9), 2)

    produtos.append({
        "id": fake.uuid4(),
        "nome": nome,
        "categoria": categoria,
        "preco_base": preco_base,
        "custo": custo
    })


df_produtos = pd.DataFrame(produtos)
df_produtos.to_csv(RAW_DIR / "produtos.csv", index=False)

vendas = []

nomes_produtos = [p["nome"] for p in produtos]

for _ in range(50):
    produto_nome = random.choice(nomes_produtos)
    vendas.append({
        "data": fake.date_this_year(),
        "produto": produto_nome,
        "quantidade": random.randint(1, 10),
        "valor": round(random.uniform(10, 500), 2),
        "status": random.choice(["ok", "cancelado", "CANC", "CANCEL"]),
        "cliente": fake.name(),
    })

df_vendas = pd.DataFrame(vendas)
df_vendas.to_csv(RAW_DIR / "vendas.csv", index=False)