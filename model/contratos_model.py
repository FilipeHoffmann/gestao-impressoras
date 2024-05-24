from static.scripts import conector_banco_de_dados

class contratos_model:
    def __init__(self) -> None:
        self.lista_contratos = None
        self.listar_todos_contratos = "SELECT * FROM contracts"
        
    def consultar_contratos(self,query):
        bd = conector_banco_de_dados.conector_banco_de_dados(query)
        self.lista_contratos = bd.consultar()
        return self.lista_contratos
    
    def criar_contrato(self,query):
        bd = conector_banco_de_dados.conector_banco_de_dados(query)
        bd.incluir()