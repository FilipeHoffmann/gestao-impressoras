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
        impressoras = query.consultar()
        return render_template('impressoras/editar_impressora.html', id_impressora=id_impressora, impressora=impressoras)
    
    def editar_impressora(id_impressora):
        modelo = request.form['modelo']
        marca = request.form['marca']
        localizacao = request.form['localizacao']
        status = request.form['status']
        tipo_impressora = request.form['tipo_impressora']
        id_setores = request.form['id_setores']
        id_cotas = request.form['id_cotas']
        update_query = f"""
            UPDATE contratos
            SET descricao = '{modelo}', data_inicial = '{marca}', data_final = '{localizacao}', status = '{status}', tipo_impressora = '{tipo_impressora}', id_setores = '{id_setores}', id_cotas = '{id_cotas}'
            WHERE id_contratos = '{id_impressora}'
        """
        conector_banco_de_dados.conector_banco_de_dados(update_query).alterar_incluir_excluir()
        return redirect(url_for('impressoras'))
            
    def excluir_contrato(id_contrato):
        delete_query = f"DELETE FROM contratos WHERE id_contratos = {id_contrato}"
        conector_banco_de_dados.conector_banco_de_dados(delete_query).alterar_incluir_excluir()
        return redirect(url_for('contratos'))
    
    def criar_impressora():
        modelo = request.form['modelo']
        marca = request.form['marca']
        localizacao = request.form['localizacao']
        status = request.form['status']
        tipo_impressora = request.form['tipo_impressora']
        id_setores = request.form['id_setores']
        id_cotas = request.form['id_cotas']
        if id_setores == '' and id_cotas == '':
            conector_banco_de_dados.conector_banco_de_dados(f'INSERT INTO impressoras(modelo, marca, localizacao, status, tipo_impressora) VALUES ("{modelo}","{marca}","{localizacao}","{status}","{tipo_impressora}")').alterar_incluir_excluir()
        elif id_setores == '':
            conector_banco_de_dados.conector_banco_de_dados(f'INSERT INTO impressoras(modelo, marca, localizacao, status, tipo_impressora, id_cotas) VALUES ("{modelo}","{marca}","{localizacao}","{status}", "{tipo_impressora}", "{id_cotas}")').alterar_incluir_excluir()
        elif id_cotas == '':
            conector_banco_de_dados.conector_banco_de_dados(f'INSERT INTO impressoras(modelo, marca, localizacao, status, tipo_impressora, id_setores) VALUES ("{modelo}","{marca}","{localizacao}","{status}", "{tipo_impressora}","{id_setores}")').alterar_incluir_excluir()
        else:
            conector_banco_de_dados.conector_banco_de_dados(f'INSERT INTO impressoras(modelo, marca, localizacao, status, tipo_impressora, id_setores, id_cotas) VALUES ("{modelo}","{marca}","{localizacao}","{status}", {tipo_impressora},"{id_setores}", "{id_cotas}")').alterar_incluir_excluir()
        mensagem = "Impressora adicionada!"
        return render_template('/impressoras/criar_impressora.html',
                            mensagem = mensagem)
    
    def obter_formulario_impressora():
        return render_template('/impressoras/criar_impressora.html')