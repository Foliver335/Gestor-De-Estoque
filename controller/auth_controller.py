from model.user_model import UserModel

class AuthController:
    def __init__(self):
        self.model = UserModel()
        self.model.create_table()

    def create_user(self, *args):
        # retorna o secret pra gerar o QR
        return self.model.add_user(*args)

    def login(self, username, password, token):
        user = self.model.authenticate(username, password)
        if not user:
            return None
        user_id, user_name, secret = user
        if not self.model.verify_totp(secret, token):
            return None
        return (user_id, user_name)
