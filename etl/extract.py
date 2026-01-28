from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"

vendas = pd.read_csv(RAW_DIR / "vendas.csv")
clientes = pd.read_csv(RAW_DIR / "clientes.csv")
produtos = pd.read_csv(RAW_DIR / "produtos.csv")

