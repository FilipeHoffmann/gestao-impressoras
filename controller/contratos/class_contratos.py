from flask import render_template, request, url_for, redirect
from static.scripts import conector_banco_de_dados

class class_contratos:
    @staticmethod
    def contratos():
        query = conector_banco_de_dados.conector_banco_de_dados("SELECT * FROM contrato")
        lista_contratos = query.consultar()
        return render_template('/contratos/contratos.html',
                            contratos = lista_contratos,
                            ids=lista_contratos)

    def obter_contrato(id_contrato):
        contrato = conector_banco_de_dados.conector_banco_de_dados(f"SELECT * FROM contrato WHERE id_contrato = {id_contrato}").consultar()
        if contrato:
            contrato = contrato[0]
            contrato_dict = {
                'data_inicial': contrato[1],
                'data_final': contrato[2],
                'data_final_atual': contrato[3]
            }
            return render_template('contratos/editar_contrato.html', contrato=contrato_dict)