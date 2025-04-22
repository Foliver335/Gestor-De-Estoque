from model.material_model import MaterialModel

class MaterialController:
    def __init__(self):
        self.model = MaterialModel()
        self.model.create_table()

    def cadastrar(self, codigo, nome, quantidade, unidade, descricao, validade):
        self.model.cadastrar_material(codigo, nome, quantidade, unidade, descricao, validade)

    def entrada_material(self, codigo, quantidade):
        self.model.atualizar_quantidade(codigo, quantidade, operacao='+')

    def saida_material(self, codigo, quantidade):
        self.model.atualizar_quantidade(codigo, quantidade, operacao='-')

    def buscar_material(self, codigo):
        return self.model.buscar_por_codigo(codigo)
