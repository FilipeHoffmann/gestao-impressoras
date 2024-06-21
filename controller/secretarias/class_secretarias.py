from flask import render_template, request, url_for, redirect
from static.scripts import conector_banco_de_dados

class class_secretarias:
    @staticmethod
    def secretarias():
        query = conector_banco_de_dados.conector_banco_de_dados("SELECT * FROM secretaria")
        lista_secretarias = query.consultar()
        return render_template('/secretarias/secretarias.html',
                            secretaria = lista_secretarias)

    def obter_secretaria(id_secretaria):
        secretaria = conector_banco_de_dados.conector_banco_de_dados(f"SELECT * FROM secretaria WHERE id_secretaria = {id_secretaria}").consultar()
        if secretaria:
            secretaria = secretaria[0]
            secretaria_dict = {
                'secretaria': secretaria[1]
            }
            return render_template('secretarias/editar_secretarias.html', secretaria=secretaria_dict)
        
    def editar_secretaria(id_secretaria):
        dados_formulario = request.form
        secretaria = dados_formulario.get('secretaria')
        
        query_editar_secretaria = f'''
        UPDATE `mydb`.`secretaria`
        SET
        `secretaria` = "{secretaria}"
        WHERE `id_secretaria` = "{id_secretaria}";
        '''
        
        conector_banco_de_dados.conector_banco_de_dados(query_editar_secretaria).alterar_incluir_excluir()
        return redirect('/secretarias')
    
    def excluir_secretaria(id_secretaria):
        query_deletar_secretaria = f'''
        DELETE FROM `mydb`.`secretaria`
        WHERE "{id_secretaria}" = id_secretaria;
        '''
        
        conector_banco_de_dados.conector_banco_de_dados(query_deletar_secretaria).alterar_incluir_excluir()
        return redirect('/secretarias')
    
    def obter_formulario_secretaria():
        return render_template('secretarias/criar_secretarias.html')
    
    def criar_secretaria():
        dados_formulario = request.form
        secretaria = dados_formulario.get('secretaria')

        query_criar_secretaria = f'''
        INSERT INTO `mydb`.`secretaria`
        (`secretaria`)
        VALUES
        ("{secretaria}");
        '''
        
        conector_banco_de_dados.conector_banco_de_dados(query_criar_secretaria).alterar_incluir_excluir()
        return redirect('/secretarias')