from static.scripts import conector_banco_de_dados

class contratos_model:
    def __init__(self) -> None:
        self.lista_contratos = None
        self.listar_contratos = "SELECT * FROM contracts"
        
    def consultar_contratos(self):
        bd = conector_banco_de_dados.conector_banco_de_dados(self.listar_contratos)
        self.lista_contratos = bd.consultar()
        return self.lista_contratos