from flask import render_template, request, url_for, redirect
from static.scripts import conector_banco_de_dados

class class_contratos:
    @staticmethod
    def contratos():
        query = conector_banco_de_dados.conector_banco_de_dados("SELECT * FROM contrato")
        lista_contratos = query.consultar()
        return render_template('/contratos/contratos.html',
                            contratos = lista_contratos)

    def obter_contrato(id_contrato):
        contrato = conector_banco_de_dados.conector_banco_de_dados(f"SELECT * FROM contratos WHERE id_contratos = {id_contrato}").consultar()
        if contrato:
            contrato = contrato[0]
            contrato_dict = {
                'descricao': contrato[1],
                'data_inicio': contrato[2],
                'data_fim': contrato[3],
                'contratada': contrato[4],
                'custo_total': contrato[5]
            }
            return render_template('contratos/editar_contrato.html', contrato=contrato_dict)
    
    def editar_contrato(id_contrato):
        descricao = request.form['descricao']
        data_inicio = request.form['data_inicio']
        data_fim = request.form['data_fim']
        contratada = request.form['contratada']
        custo_total = request.form['custo_total']
        update_query = f"""
            UPDATE contratos
            SET descricao = '{descricao}', data_inicial = '{data_inicio}', data_final = '{data_fim}', contratada = '{contratada}', custo_total = '{custo_total}'
            WHERE id_contratos = '{id_contrato}'
        """
        conector_banco_de_dados.conector_banco_de_dados(update_query).alterar_incluir_excluir()
        return redirect(url_for('contratos'))
            
    def excluir_contrato(id_contrato):
        delete_query = f"DELETE FROM contratos WHERE id_contratos = {id_contrato}"
        conector_banco_de_dados.conector_banco_de_dados(delete_query).alterar_incluir_excluir()
        return redirect(url_for('contratos'))
    
    def criar_contrato():
        descricao = request.form['descricao']
        data_inicio = request.form['data_inicio']
        data_fim = request.form['data_fim']
        contratada = request.form['contratada']
        custo_total = request.form['custo_total']
        conector_banco_de_dados.conector_banco_de_dados(f'INSERT INTO contratos(descricao,data_final,data_inicial,custo_total,contratada) VALUES ("{descricao}","{data_fim}","{data_inicio}","{custo_total}","{contratada}")').alterar_incluir_excluir()
        mensagem = "Contrato adicionado!"
        return render_template('/contratos/criar_contrato.html',
                            mensagem = mensagem)
    
    def obter_formulario_contrato():
        return render_template('/contratos/criar_contrato.html')