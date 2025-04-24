from model.db_connection import get_connection

class UserModel:
    def create_table(self):
        conn = get_connection(); cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id           SERIAL PRIMARY KEY,
            username     VARCHAR(50) UNIQUE NOT NULL,
            password     VARCHAR(255) NOT NULL,
            first_name   VARCHAR(100) NOT NULL,
            last_name    VARCHAR(100) NOT NULL,
            matricula    VARCHAR(50)  NOT NULL,
            cpf          VARCHAR(20)  UNIQUE NOT NULL,
            patente      VARCHAR(50)  NOT NULL,
            totp_secret  VARCHAR(32)  NOT NULL
        );
        """)
        conn.commit(); cur.close(); conn.close()

    def exists(self, username, cpf):
        conn = get_connection(); cur = conn.cursor()
        cur.execute("""
            SELECT 1 FROM users
             WHERE username = %s OR cpf = %s
        """, (username, cpf))
        found = cur.fetchone() is not None
        cur.close(); conn.close()
        return found

    def add_user(self, username, password,
                 first_name, last_name,
                 matricula, cpf, patente):
        import pyotp
        secret = pyotp.random_base32()
        conn = get_connection(); cur = conn.cursor()
        cur.execute("""
        INSERT INTO users (
            username, password,
            first_name, last_name,
            matricula, cpf, patente,
            totp_secret
        ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT (username) DO NOTHING;
        """, (username, password,
              first_name, last_name,
              matricula, cpf, patente,
              secret))
        conn.commit(); cur.close(); conn.close()
        return secret

    def authenticate(self, username, password):
        # retorna (id, username, secret) ou None
        conn = get_connection(); cur = conn.cursor()
        cur.execute("""
        SELECT id, username, totp_secret
          FROM users
         WHERE username=%s AND password=%s
        """, (username, password))
        row = cur.fetchone()
        cur.close(); conn.close()
        return row

    def verify_totp(self, secret, token):
        import pyotp
        totp = pyotp.TOTP(secret)
        return totp.verify(token, valid_window=1)
