from flask import render_template, request, url_for, redirect
from static.scripts import conector_banco_de_dados

class class_contratos:
    @staticmethod
    def contratos():
        query = conector_banco_de_dados.conector_banco_de_dados("SELECT * FROM contrato")
        lista_contratos = query.consultar()
        return render_template('/contratos/contratos.html',
                            contrato = lista_contratos)

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
        
    def editar_contrato(id_contrato):
        dados_formulario = request.form
        data_inicial = dados_formulario.get('data_inicial')
        data_final = dados_formulario.get('data_final')
        data_final_atual = dados_formulario.get('data_final_atual')
        
        query_editar_contrato = f'''
        UPDATE `mydb`.`contrato`
        SET
        `data_inicial` = "{data_inicial}",
        `data_final` = "{data_final}",
        `data_final_atual` = "{data_final_atual}"
        WHERE `id_contrato` = "{id_contrato}";
        '''
        
        conector_banco_de_dados.conector_banco_de_dados(query_editar_contrato).alterar_incluir_excluir()
        return redirect('/contratos')
    
    def excluir_contrato(id_contato):
        query_deletar_contrato = f'''
        DELETE FROM `mydb`.`contrato`
        WHERE "{id_contato}" = id_contrato;
        '''
        
        conector_banco_de_dados.conector_banco_de_dados(query_deletar_contrato).alterar_incluir_excluir()
        return redirect('/contratos')
    
    def obter_formulario_contrato():
        return render_template('contratos/criar_contrato.html')
    
    def criar_contrato():
        dados_formulario = request.form
        data_inicial = dados_formulario.get('data_inicial')
        data_final = dados_formulario.get('data_final')
        data_final_atual = dados_formulario.get('data_final_atual')

        query_criar_contrato = f'''
        INSERT INTO `mydb`.`contrato`
        (`data_inicial`,
        `data_final`,
        `data_final_atual`)
        VALUES
        ("{data_inicial}",
        "{data_final}",
        "{data_final_atual}");
        '''
        
        conector_banco_de_dados.conector_banco_de_dados(query_criar_contrato).alterar_incluir_excluir()
        return redirect('/contratos')