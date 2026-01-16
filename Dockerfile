# Usar uma imagem oficial do Python
FROM python:3.11-slim

# Definir diretório de trabalho dentro do container
WORKDIR /app

# Copiar arquivos do projeto para dentro do container
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


# Comando padrão: rodar seu pipeline
CMD ["python","-m", "etl.extract"]
