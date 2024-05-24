import mysql.connector

class banco_de_dados:
    def __init__(self, query: str):
        self.conector_sql = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123321",
            database="controleimpressoras"
        )
        self.cursor = self.conector_sql.cursor()
        self.query = query

    def consultar(self):
        self.cursor.execute(self.query)
        self.resultados = self.cursor.fetchall()
        self.cursor.close()
        self.conector_sql.close()
        return self.resultados
    
    def incluir(self):
        self.cursor.execute(self.query)
        self.conector_sql.commit()
        self.cursor.close()
        self.conector_sql.close()