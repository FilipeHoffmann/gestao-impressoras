from flask import render_template, request, url_for, redirect
from static.scripts import conector_banco_de_dados

class class_secretarias:
    @staticmethod
    def secretarias():
        if request.method == "GET":
            query = conector_banco_de_dados.conector_banco_de_dados("SELECT * FROM secretarias ORDER BY id_secretarias DESC")
            secretarias = query.consultar()
            return render_template("/secretarias/secretarias.html",
                                ids = secretarias,
                                secretarias=secretarias)
            
    def criar_secretaria():
        if request.method == "POST":
            nome = request.form["nome"]
            query = f'''INSERT INTO secretarias(nome)
                    VALUES ('{nome}')'''
            conector_banco_de_dados.conector_banco_de_dados(query).alterar_incluir_excluir()
            mensagem = "Secretaria adicionada!"
            return render_template("/secretarias/criar_secretaria.html",
                                   mensagem = mensagem)

    def obter_formulario_secretaria():
        if request.method == "GET":
            return render_template("/secretarias/criar_secretaria.html")
        
    def editar_secretaria(id_secretaria):
        nome = request.form["nome"]
        update_query = f"""
            UPDATE secretarias
            SET nome = '{nome}'
            WHERE id_secretarias = '{id_secretaria}'
        """
        conector_banco_de_dados.conector_banco_de_dados(update_query).alterar_incluir_excluir()
        return redirect(url_for('secretarias'))
    
    def obter_secretaria(id_secretaria):
        if request.method == 'GET':
            secretaria = conector_banco_de_dados.conector_banco_de_dados(f"SELECT * FROM secretarias WHERE id_secretarias = {id_secretaria}").consultar()
            if secretaria:
                secretaria = secretaria[0]
                secretaria_dict = {
                    'nome': secretaria[1],
                }
                return render_template('secretarias/editar_secretaria.html', secretaria=secretaria_dict)
    
    def excluir_secretaria(id_secretaria):
        delete_query = f"DELETE FROM secretarias WHERE id_secretarias = {id_secretaria}"
        conector_banco_de_dados.conector_banco_de_dados(delete_query).alterar_incluir_excluir()
        return redirect(url_for('secretarias'))