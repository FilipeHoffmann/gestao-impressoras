from flask import render_template, request, url_for, redirect
from static.scripts import conector_banco_de_dados

class class_aditivos:
    @staticmethod
    def aditivos():
        lista_aditivos = conector_banco_de_dados.conector_banco_de_dados("SELECT * FROM aditivos ORDER BY id_aditivos DESC").consultar()
        return render_template('/contratos/aditivos/aditivos.html',
                            aditivos = lista_aditivos,
                            ids=lista_aditivos)
            
    def criar_aditivo():
        id_contrato = request.form['id_contrato']
        data_prorrogada = request.form['data_prorrogada']
        detalhes = request.form['detalhes']
        custo_adicional = request.form['custo_adicional']
        conector_banco_de_dados.conector_banco_de_dados(f'INSERT INTO aditivos(id_contratos,data_aditivo,detalhes,custo_adicional) VALUES ("{id_contrato}","{data_prorrogada}","{detalhes}","{custo_adicional}")').alterar_incluir_excluir()
        mensagem = "Contrato adicionado!"
        return render_template('/contratos/aditivos/criar_aditivo.html',
                            mensagem = mensagem)
            
    def obter_formulario_aditivo():
        return render_template('/contratos/aditivos/criar_aditivo.html')
    
    def obter_aditivo(id_aditivo):
        aditivos = conector_banco_de_dados.conector_banco_de_dados(f"SELECT * FROM aditivos WHERE id_aditivos = {id_aditivo}").consultar()
        return render_template('/contratos/aditivos/editar_aditivo.html',  aditivo=aditivos)
        
    def editar_aditivo(id_aditivo):
        id_contrato = request.form['id_contrato']
        data_prorrogada = request.form['data_prorrogada']
        detalhes = request.form['detalhes']
        custo_adicional = request.form['custo_adicional']
        update_query = f"""
            UPDATE aditivos
            SET id_contratos = '{id_contrato}', data_aditivo = '{data_prorrogada}', detalhes = '{detalhes}', custo_adicional = '{custo_adicional}'
            WHERE id_aditivos = '{id_aditivo}'
        """
        conector_banco_de_dados.conector_banco_de_dados(update_query).alterar_incluir_excluir()
        return redirect(url_for('aditivos'))
        
    def excluir_contrato(id_aditivo):
        delete_query = f"DELETE FROM aditivos WHERE id_aditivos = {id_aditivo}"
        conector_banco_de_dados.conector_banco_de_dados(delete_query).alterar_incluir_excluir()
        return redirect(url_for('aditivos'))