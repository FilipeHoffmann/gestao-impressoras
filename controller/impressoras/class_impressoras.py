from flask import render_template, request, url_for, redirect
from static.scripts import conector_banco_de_dados

class class_impressoras:
    @staticmethod
    def impressoras():
        query = conector_banco_de_dados.conector_banco_de_dados("SELECT * FROM impressoras ORDER BY id_impressoras DESC")
        lista_impressoras = query.consultar()
        return render_template('/impressoras/impressoras.html',
                            impressoras = lista_impressoras,
                            ids=lista_impressoras)

    def obter_impressora(id_impressora):
        query = conector_banco_de_dados.conector_banco_de_dados(f"SELECT * FROM impressoras WHERE id_impressoras = {id_impressora}")
        impressora = query.consultar()
        return render_template('impressoras/editar_impressora.html', id_impressora=id_impressora, impressora=impressora)
    
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
    
    def criar_impressora():
        modelo = request.form['modelo']
        marca = request.form['marca']
        localizacao = request.form['localizacao']
        status = request.form['status']
        id_setores = request.form['id_setores']
        id_cotas = request.form['id_cotas']
        conector_banco_de_dados.conector_banco_de_dados(f'INSERT INTO impressoras(modelo, marca, localizacao, status, id_setores, id_cotas) VALUES ("{modelo}","{marca}","{localizacao}","{status}","{id_setores}", "{id_cotas}")').alterar_incluir_excluir()
        mensagem = "Impressora adicionada!"
        return render_template('/impressoras/criar_impressora.html',
                            mensagem = mensagem)
    
    def obter_formulario_contrato():
        return render_template('/contratos/criar_contrato.html')