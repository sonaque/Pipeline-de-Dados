import pandas as pd
import random
from faker import Faker 
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"

RAW_DIR.mkdir(parents=True, exist_ok=True)


fake = Faker('pt_BR')

vendas = []

for _ in range(50):
    vendas.append({
        "data": fake.date_this_year(),
        "produto": fake.word(),
        "quantidade": random.randint(1, 10),
        "valor": round(random.uniform(10, 500), 2),
        "status": random.choice(["ok", "cancelado", "CANC", "CANCEL"]),
        "cliente": fake.name(),
    })

df_vendas = pd.DataFrame(vendas)
df_vendas.to_csv(RAW_DIR / "vendas.csv", index=False)

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

for _ in range(15):
    produtos.append({
        "id": fake.uuid4(),
        "categoria": random.choice(["Eletrônicos", "Moda", "Alimentos", "Eletrônicos", "Eletronic"]),
        "preco_base": round(random.uniform(50, 2000), 2),
        "custo": round(random.uniform(-50, 1500), 2)
    })

df_produtos = pd.DataFrame(produtos)
df_produtos.to_csv(RAW_DIR / "produtos.csv", index=False)