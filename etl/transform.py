import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

vendas = pd.read_csv(RAW_DIR / "vendas.csv")
clientes = pd.read_csv(RAW_DIR / "clientes.csv")
produtos = pd.read_csv(RAW_DIR / "produtos.csv")

vendas ["status"] = vendas ["status"].str.lower().replace({
    "cancel" : "Cancelado",
    "canc" : "Cancelado",
    "cancelado" : "Cancelado",
    "ok" : "Concluido"
})

vendas["valor"] = (
    pd.to_numeric(vendas["valor"], errors="coerce")
      .round(2)
)


clientes["estado"] = clientes["estado"].replace({
    "São Paulo": "SP",
    "S.P.": "SP",
    "Rio de Janeiro": "RJ"
})

produtos["categoria"] = produtos["categoria"].replace({
    "Eletronic": "Eletrônicos"
})

produtos["preco_base"] = (
    pd.to_numeric(produtos["preco_base"], errors="coerce")
      .round(2)
)

produtos.loc[produtos["custo"] < 0, "custo"] = None

vendas.drop_duplicates(inplace=True) 
clientes.drop_duplicates(inplace=True) 
produtos.drop_duplicates(inplace=True)

vendas.to_csv(PROCESSED_DIR / "vendas_clean.csv", index=False)
clientes.to_csv(PROCESSED_DIR / "clientes_clean.csv", index=False)
produtos.to_csv(PROCESSED_DIR / "produtos_clean.csv", index=False)