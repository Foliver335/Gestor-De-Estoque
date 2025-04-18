import psycopg2
from psycopg2 import OperationalError

try:
    conn = psycopg2.connect(
        host="127.0.0.1",
        port=5432,
        database="Materiais",
        user="postgres",
        password="root"
    )
    print("✅ Conexão bem‑sucedida!")
    conn.close()
except OperationalError as e:
    print("❌ Erro de conexão:", e)
