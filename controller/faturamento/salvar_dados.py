import csv

class salvar_dados:
    def __init__(self,dados:list, nome_arquivo:str):
        self.nome_arquivo = nome_arquivo
        self.dados_array = dados
    
    def verifica_arquivo(self):
        try:
            f = open(self.nome_arquivo)
            f.close()
            return True
        except:
            return False
        
    def salvar(self): 
        with open(f'temp/{self.nome_arquivo}','w+', encoding='utf-8', newline='') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            escritor_csv.writerow(["SECRETARIA","SETOR","IMPRESSORA","TIPO COTA","STATUS","DATA COLETA","PÁGINAS IMPRESSAS","COTA","VALOR EXCEDENTES","CÓPIAS EXCEDENTES","TOTAL A PAGAR"])
            for i in range(len(self.dados_array)):
                escritor_csv.writerow(self.dados_array[i])

            