from flask import render_template, request, url_for, redirect
from static.scripts import conector_banco_de_dados

class class_itens:
    @staticmethod
    def itens():
        query = conector_banco_de_dados.conector_banco_de_dados("SELECT * FROM item")
        lista_itens = query.consultar()
        query_contratos = conector_banco_de_dados.conector_banco_de_dados("SELECT * FROM contrato")
        lista_contratos = query_contratos.consultar()
        return render_template('/itens/itens.html',
                            item = lista_itens,
                            contratos = lista_contratos)

    def criar_item():
        dados_formulario = request.form
        id_item = dados_formulario.get('id_item')
        descricao = dados_formulario.get('descricao')
        franquia_pb = dados_formulario.get('franquia_pb')
        franquia_color = dados_formulario.get('franquia_color')
        tipo = dados_formulario.get('tipo')
        copia_locacao = dados_formulario.get('copia_locacao')
        color = dados_formulario.get('color')
        
        query_criar_item = f'''
        INSERT INTO `mydb`.`item`
        (`id_item`,
        `descricao`,
        `franquia_pb`,
        `franquia_color`,
        `tipo`,
        `copia_locacao`,
        `color`)
        VALUES ("{id_item}",
        "{descricao}",
        "{franquia_pb}",
        "{franquia_color}",
        "{tipo}",
        "{copia_locacao}",
        "{color}");
        '''
        
        conector_banco_de_dados.conector_banco_de_dados(query_criar_item).alterar_incluir_excluir()
        return redirect('/itens')