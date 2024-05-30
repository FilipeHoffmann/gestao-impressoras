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
        if impressoras:
                impressoras = impressoras[0]
                impressoras_dict = {
                    'modelo': impressoras[1],
                    'marca': impressoras[2],
                    'localizacao': impressoras[3],
                    'status': impressoras[4],
                    'tipo_impressora': impressoras[5],
                    'id_setores': impressoras[6],
                    'id_cotas': impressoras[7]
                }
        return render_template('impressoras/editar_impressora.html', id_impressora=id_impressora, impressora=impressoras_dict)
    
    def editar_impressora(id_impressora):
        modelo = request.form['modelo']
        marca = request.form['marca']
        localizacao = request.form['localizacao']
        status = request.form['status']
        tipo_impressora = request.form['tipo_impressora']
        id_setores = request.form['id_setores']
        id_cotas = request.form['id_cotas']
        if ((id_setores == '' and id_cotas == '') or (id_setores == "None" and id_cotas == "None")):
            update_query = f"""
            UPDATE impressoras
            SET modelo = '{modelo}', marca = '{marca}', localizacao = '{localizacao}', status = '{status}', tipo_impressora = '{tipo_impressora}'
            WHERE id_impressoras = '{id_impressora}'
            """
        elif (id_setores == '' or id_setores == "None"):
            update_query = f"""
            UPDATE impressoras
            SET modelo = '{modelo}', marca = '{marca}', localizacao = '{localizacao}', status = '{status}', tipo_impressora = '{tipo_impressora}', id_cotas = '{id_cotas}'
            WHERE id_impressoras = '{id_impressora}'
            """
        elif (id_cotas == '' or id_cotas == "None"):
            update_query = f"""
            UPDATE impressoras
            SET modelo = '{modelo}', marca = '{marca}', localizacao = '{localizacao}', status = '{status}', tipo_impressora = '{tipo_impressora}', id_setores = '{id_setores}'
            WHERE id_impressoras = '{id_impressora}'
            """
        conector_banco_de_dados.conector_banco_de_dados(update_query).alterar_incluir_excluir()
        return redirect(url_for('impressoras'))
            
    def excluir_impressora(id_impressora):
        delete_query = f"DELETE FROM impressoras WHERE id_impressoras = {id_impressora}"
        conector_banco_de_dados.conector_banco_de_dados(delete_query).alterar_incluir_excluir()
        return redirect(url_for('impressoras'))
    
    def criar_impressora():
        id_impressora = request.form['id_impressora']
        modelo = request.form['modelo']
        marca = request.form['marca']
        localizacao = request.form['localizacao']
        status = request.form['status']
        tipo_impressora = request.form['tipo_impressora']
        id_setores = request.form['id_setores']
        id_cotas = request.form['id_cotas']
        if id_setores == '' and id_cotas == '':
            conector_banco_de_dados.conector_banco_de_dados(f'INSERT INTO impressoras(id_impressoras, modelo, marca, localizacao, status, tipo_impressora) VALUES ("{id_impressora}","{modelo}","{marca}","{localizacao}","{status}","{tipo_impressora}")').alterar_incluir_excluir()
        elif id_setores == '':
            conector_banco_de_dados.conector_banco_de_dados(f'INSERT INTO impressoras(id_impressoras, modelo, marca, localizacao, status, tipo_impressora, id_cotas) VALUES ("{id_impressora}","{modelo}","{marca}","{localizacao}","{status}", "{tipo_impressora}", "{id_cotas}")').alterar_incluir_excluir()
        elif id_cotas == '':
            conector_banco_de_dados.conector_banco_de_dados(f'INSERT INTO impressoras(id_impressoras, modelo, marca, localizacao, status, tipo_impressora, id_setores) VALUES ("{id_impressora}","{modelo}","{marca}","{localizacao}","{status}", "{tipo_impressora}","{id_setores}")').alterar_incluir_excluir()
        else:
            conector_banco_de_dados.conector_banco_de_dados(f'INSERT INTO impressoras(id_impressoras, modelo, marca, localizacao, status, tipo_impressora, id_setores, id_cotas) VALUES ("{id_impressora}","{modelo}","{marca}","{localizacao}","{status}", {tipo_impressora},"{id_setores}", "{id_cotas}")').alterar_incluir_excluir()
        mensagem = "Impressora adicionada!"
        return render_template('/impressoras/criar_impressora.html',
                            mensagem = mensagem)
    
    def obter_formulario_impressora():
        return render_template('/impressoras/criar_impressora.html')