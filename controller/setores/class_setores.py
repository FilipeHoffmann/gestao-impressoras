from flask import render_template, request, url_for, redirect
from static.scripts import conector_banco_de_dados

class class_setores:
    @staticmethod
    def setores():
        lista_setores = conector_banco_de_dados.conector_banco_de_dados("SELECT * FROM setores ORDER BY id_setores DESC").consultar()
        return render_template('/secretarias/setores/setores.html',
                            setores = lista_setores,
                            ids=lista_setores)
            
    def criar_setor():
        id_secretaria = request.form['id_secretaria']
        nome_setor = request.form['nome_setor']
        endereco = request.form['endereco']
        conector_banco_de_dados.conector_banco_de_dados(f'INSERT INTO setores(id_secretarias,nome_setor,endereco) VALUES ("{id_secretaria}","{nome_setor}","{endereco}")').alterar_incluir_excluir()
        mensagem = "Setor adicionado!"
        return render_template('/secretarias/setores/criar_setor.html',
                            mensagem = mensagem)
            
    def obter_formulario_setor():
        return render_template('/secretarias/setores/criar_setor.html')
    
    def obter_setor(id_setor):
        setor = conector_banco_de_dados.conector_banco_de_dados(f"SELECT * FROM setores WHERE id_setores = {id_setor}").consultar()
        if setor:
            setor = setor[0]
            setor_dict = {
                'id_secretaria': setor[1],
                'nome_setor': setor[2],
                'endereco': setor[3]
            }
            return render_template('/secretarias/setores/editar_setor.html', setor=setor_dict)
        
    def editar_setor(id_setor):
        id_secretaria = request.form['id_secretaria']
        nome_setor = request.form['nome_setor']
        endereco = request.form['endereco']

        update_query = f"""
            UPDATE setores
            SET id_secretarias = '{id_secretaria}', nome_setor = '{nome_setor}', endereco = '{endereco}'
            WHERE id_setores = '{id_setor}'
        """
        conector_banco_de_dados.conector_banco_de_dados(update_query).alterar_incluir_excluir()
        return redirect(url_for('setores'))
        
    def excluir_setor(id_setor):
        delete_query = f"DELETE FROM setores WHERE id_setores = {id_setor}"
        conector_banco_de_dados.conector_banco_de_dados(delete_query).alterar_incluir_excluir()
        return redirect(url_for('setores'))