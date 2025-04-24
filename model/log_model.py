from model.db_connection import get_connection

class LogModel:
    def create_table(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id               SERIAL PRIMARY KEY,
            material_id      INTEGER NOT NULL,
            material_codigo  VARCHAR(100) NOT NULL,
            material_nome    VARCHAR(100) NOT NULL,
            user_id          INTEGER NOT NULL,
            username         VARCHAR(50)  NOT NULL,
            quantidade       INTEGER NOT NULL,
            timestamp        TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)
        conn.commit(); cur.close(); conn.close()

    def log_retirada(self, material_id, material_codigo,
                     material_nome, user_id, username, quantidade):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
        INSERT INTO logs (
            material_id,
            material_codigo,
            material_nome,
            user_id,
            username,
            quantidade
        ) VALUES (%s,%s,%s,%s,%s,%s)
        """, (material_id, material_codigo,
              material_nome, user_id,
              username, quantidade))
        conn.commit(); cur.close(); conn.close()
