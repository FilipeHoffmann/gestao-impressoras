from flask import render_template, request, url_for, redirect
from static.scripts import conector_banco_de_dados

class class_cotas:
    @staticmethod
    def cotas():
        query = conector_banco_de_dados.conector_banco_de_dados("SELECT * FROM cotas ORDER BY id_cotas DESC")
        lista_cotas = query.consultar()
        return render_template('impressoras/cotas/cotas.html',
                            cotas = lista_cotas,
                            ids=lista_cotas)

    def obter_cota(id_cota):
        query = conector_banco_de_dados.conector_banco_de_dados(f"SELECT * FROM cotas WHERE id_cotas = {id_cota}")
        cotas = query.consultar()
        if cotas:
                cotas = cotas[0]
                cotas_dict = {
                    'cota_mensal': cotas[1],
                    'tipo_cota': cotas[2]
                }
        return render_template('impressoras/cotas/editar_cota.html', id_cota=id_cota, cotas=cotas_dict)
    
    def editar_cota(id_cota):
        cota_mensal = request.form['cota_mensal']
        tipo_cota = request.form['tipo_cota']
        update_query = f"""
        UPDATE cotas
        SET cota_mensal = "{cota_mensal}", tipo_cota = '{tipo_cota}'
        WHERE id_cotas = '{id_cota}'
        """
        conector_banco_de_dados.conector_banco_de_dados(update_query).alterar_incluir_excluir()
        return redirect(url_for('cotas'))
            
    def excluir_cota(id_cota):
        delete_query = f"DELETE FROM cotas WHERE id_cotas = {id_cota}"
        conector_banco_de_dados.conector_banco_de_dados(delete_query).alterar_incluir_excluir()
        return redirect(url_for('cotas'))
    
    def criar_cota():
        cota_mensal = request.form['cota_mensal']
        tipo_cota = request.form['tipo_cota']
        conector_banco_de_dados.conector_banco_de_dados(f'INSERT INTO cotas(cota_mensal,tipo_cota) VALUES ("{cota_mensal}","{tipo_cota}")').alterar_incluir_excluir()
        mensagem = "Cota adicionada!"
        return render_template('impressoras/cotas/criar_cota.html',
                            mensagem = mensagem)
    
    def obter_formulario_cota():
        query = conector_banco_de_dados.conector_banco_de_dados(f"SELECT * FROM impressoras")
        ids = query.consultar()
        return render_template('impressoras/cotas/criar_cota.html',
                               ids=ids)