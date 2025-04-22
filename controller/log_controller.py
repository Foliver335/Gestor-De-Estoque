from model.log_model import LogModel

class LogController:
    def __init__(self):
        self.model = LogModel()
        self.model.create_table()

    def registrar_log_saida(self, material, user, quantidade):
        self.model.log_retirada(
            material[0],   # material_id
            material[1],   # codigo
            material[2],   # nome
            user[0],       # user_id
            user[1],       # username
            quantidade
        )
