import psycopg2
from psycopg2 import OperationalError

def get_connection():
    try:
        return psycopg2.connect(
            host="127.0.0.1",             
            port=5432,                   
            database="Materiais",   
            user="postgres",
            password="root"
        )
    except OperationalError as e:
        raise RuntimeError(f"Erro ao conectar no PostgreSQL: {e}")
