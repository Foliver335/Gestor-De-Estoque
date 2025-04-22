from model.db_connection import get_connection

class MaterialModel:
    def create_table(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS materiais (
                id        SERIAL PRIMARY KEY,
                codigo    VARCHAR(100) UNIQUE NOT NULL,
                nome      VARCHAR(100) NOT NULL,
                quantidade INTEGER NOT NULL,
                unidade   VARCHAR(50),
                descricao TEXT,
                validade  DATE
            );
        """)
        conn.commit()
        cur.close()
        conn.close()

    def cadastrar_material(self, codigo, nome, quantidade, unidade, descricao, validade):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO materiais (codigo, nome, quantidade, unidade, descricao, validade)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (codigo) DO NOTHING;
        """, (codigo, nome, quantidade, unidade, descricao, validade))
        conn.commit()
        cur.close()
        conn.close()

    def atualizar_quantidade(self, codigo, quantidade, operacao='+'):
        conn = get_connection()
        cur = conn.cursor()
        if operacao == '+':
            cur.execute(
                "UPDATE materiais SET quantidade = quantidade + %s WHERE codigo = %s",
                (quantidade, codigo)
            )
        else:
            cur.execute(
                "UPDATE materiais SET quantidade = quantidade - %s WHERE codigo = %s",
                (quantidade, codigo)
            )
        conn.commit()
        cur.close()
        conn.close()

    def buscar_por_codigo(self, codigo):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, codigo, nome, quantidade, unidade, descricao, validade FROM materiais WHERE codigo = %s", (codigo,))
        resultado = cur.fetchone()
        cur.close()
        conn.close()
        return resultado
