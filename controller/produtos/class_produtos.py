from flask import render_template, request, url_for, redirect
from static.scripts import conector_banco_de_dados

class class_produtos:
    @staticmethod
    def produtos():
        query = conector_banco_de_dados.conector_banco_de_dados("SELECT * FROM produto")
        lista_produtos = query.consultar()
        return render_template('/produtos/produtos.html',
                            produto = lista_produtos)

    def obter_produto(id_produto):
        produto = conector_banco_de_dados.conector_banco_de_dados(f"SELECT * FROM produto WHERE id_produto = {id_produto}").consultar()
        if produto:
            produto = produto[0]
            produto_dict = {
                'descricao': produto[1],
                'franquia_pb': produto[2],
                'franquia_color': produto[3],
                'tipo': produto[4],
                'copia_locacao': produto[5],
                'color': produto[6]
            }
            return render_template('produtos/editar_produtos.html', produto=produto_dict)
        
    def editar_produto(id_produto):
        dados_formulario = request.form
        descricao = dados_formulario.get('descricao')
        franquia_pb = dados_formulario.get('franquia_pb')
        franquia_color = dados_formulario.get('franquia_color')
        tipo = dados_formulario.get('tipo')
        copia_locacao = dados_formulario.get('copia_locacao')
        color = dados_formulario.get('color')
        
        query_editar_produto = f'''
        UPDATE `mydb`.`produto`
        SET
        `descricao` = "{descricao}",
        `franquia_pb` = "{franquia_pb}",
        `franquia_color` = "{franquia_color}",
        `tipo` = "{tipo}",
        `copia_locacao` = "{copia_locacao}",
        `color` = "{color}"
        WHERE `id_produto` = "{id_produto}";
        '''
        
        conector_banco_de_dados.conector_banco_de_dados(query_editar_produto).alterar_incluir_excluir()
        return redirect('/produtos')
    
    def excluir_produto(id_produto):
        query_deletar_produto = f'''
        DELETE FROM `mydb`.`produto`
        WHERE "{id_produto}" = id_produto;
        '''
        
        conector_banco_de_dados.conector_banco_de_dados(query_deletar_produto).alterar_incluir_excluir()
        return redirect('/produtos')
    
    def obter_formulario_produto():
        return render_template('produtos/criar_produtos.html')
    
    def criar_produto():
        dados_formulario = request.form
        id_produto = dados_formulario.get('id_produto')
        descricao = dados_formulario.get('descricao')
        franquia_pb = dados_formulario.get('franquia_pb')
        franquia_color = dados_formulario.get('franquia_color')
        tipo = dados_formulario.get('tipo')
        copia_locacao = dados_formulario.get('copia_locacao')
        color = dados_formulario.get('color')
        
        query_criar_produto = f'''
        INSERT INTO `mydb`.`produto`
        (`id_produto`,
        `descricao`,
        `franquia_pb`,
        `franquia_color`,
        `tipo`,
        `copia_locacao`,
        `color`)
        VALUES ("{id_produto}",
        "{descricao}",
        "{franquia_pb}",
        "{franquia_color}",
        "{tipo}",
        "{copia_locacao}",
        "{color}");
        '''
        
        conector_banco_de_dados.conector_banco_de_dados(query_criar_produto).alterar_incluir_excluir()
        return redirect('/produtos')