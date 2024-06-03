from flask import render_template, request, url_for, redirect
from static.scripts import conector_banco_de_dados

class class_faturamento:
    @staticmethod
    def faturamento():
        return render_template("/faturamento/faturamento.html")
    
    def obter_faturamento():
        query = '''
        SELECT c.id_contadores, secretarias.nome, setores.nome_setor, c.paginas_impressas,cotas.cota_mensal
        FROM contadores AS c
        INNER JOIN setores ON c.id_setores = setores.id_setores
        INNER JOIN secretarias ON setores.id_secretarias = secretarias.id_secretarias
        INNER JOIN impressoras ON c.id_impressoras = impressoras.id_impressoras
        INNER JOIN cotas ON impressoras.id_cotas = cotas.id_cotas
        '''