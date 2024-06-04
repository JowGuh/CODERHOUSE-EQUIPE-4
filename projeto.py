import sqlite3
import requests

# Definir a função alerta
def alerta(mensagem):
    print(f"ALERTA: {mensagem}")

# URL da API
api_url = "https://brasilapi.com.br/api/banks/v1"

# Requisição à API
response = requests.get(api_url)
data = response.json()

# Conectar ao banco de dados
conn = sqlite3.connect('bancos.db')
cursor = conn.cursor()

# Criar as tabelas
cursor.execute('''
CREATE TABLE IF NOT EXISTS bancos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    codigo TEXT,
    ispb TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS codigos_bancarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    banco_nome TEXT,
    codigo_banco TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS bancos_ispb (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    banco_nome TEXT,
    ispb TEXT
)
''')

# Inserir os dados nas tabelas
for banco in data:
    nome = banco.get('name', None)
    codigo = banco.get('code', None)
    ispb = banco.get('ispb', None)
    
    if nome and codigo and ispb:
        cursor.execute('''
        INSERT INTO bancos (nome, codigo, ispb)
        VALUES (?, ?, ?)
        ''', (nome, codigo, ispb))
        
        banco_id = cursor.lastrowid
        
        # Inserir dados na tabela de códigos bancários
        cursor.execute('''
        INSERT INTO codigos_bancarios (banco_nome, codigo_banco)
        VALUES (?, ?)
        ''', (nome, codigo))
        
        # Inserir dados na tabela de bancos por ISPB
        cursor.execute('''
        INSERT INTO bancos_ispb (banco_nome, ispb)
        VALUES (?, ?)
        ''', (nome, ispb))
    else:
        alerta(f"Dados faltando para o banco: {banco}")

# Salvar (commit) as mudanças e fechar a conexão
conn.commit()
conn.close()
