from flask import render_template, request, url_for, redirect
from static.scripts import conector_banco_de_dados

class class_produtos:
    @staticmethod
    def produtos():
        if request.method == "GET":
            query = conector_banco_de_dados.conector_banco_de_dados("SELECT * FROM produtos ORDER BY id_produtos DESC")
            produtos = query.consultar()
            return render_template("/produtos/produtos.html",
                                ids = produtos,
                                produtos=produtos)
            
    def criar_produto():
        if request.method == "POST":
            lote = request.form["lote"]
            codigo = request.form["codigo"]
            descricao = request.form["descricao"]
            unidade = request.form["unidade"]
            quantidade_mensal = request.form["quantidade_mensal"]
            quantidade_anual = request.form["quantidade_anual"]
            valor_unitario = request.form["valor_unitario"]
            valor_total = request.form["valor_total"]
            id_contratos = request.form["id_contratos"]
            id_aditivos = request.form["id_aditivos"]
            print(id_aditivos)
            print(type(id_aditivos))
            if id_aditivos == "" and id_contratos != "":
                query = f'''INSERT INTO produtos(lote,codigo,descricao,unidade,quantidade_mensal,quantidade_anual,valor_unitario,valor_total,id_contratos)
                        VALUES ('{lote}','{codigo}','{descricao}','{unidade}','{quantidade_mensal}','{quantidade_anual}','{valor_unitario}','{valor_total}','{id_contratos}')'''
            if id_contratos != "" and id_aditivos != "":
                query = f'''INSERT INTO produtos(lote,codigo,descricao,unidade,quantidade_mensal,quantidade_anual,valor_unitario,valor_total,id_contratos,id_aditivos)
                        VALUES ('{lote}','{codigo}','{descricao}','{unidade}','{quantidade_mensal}','{quantidade_anual}','{valor_unitario}','{valor_total}','{id_contratos}','{id_aditivos}')'''
            if id_contratos == "" and id_aditivos == "":
                query = f'''INSERT INTO produtos(lote,codigo,descricao,unidade,quantidade_mensal,quantidade_anual,valor_unitario,valor_total)
                        VALUES ('{lote}','{codigo}','{descricao}','{unidade}','{quantidade_mensal}','{quantidade_anual}','{valor_unitario}','{valor_total}')'''
            conector_banco_de_dados.conector_banco_de_dados(query).alterar_incluir_excluir()
            mensagem = "Produto adicionado!"
            return render_template("/produtos/criar_produto.html",
                                   mensagem = mensagem)

    def obter_formulario_produto():
        if request.method == "GET":
            contratos_query = "SELECT id_contratos,descricao FROM contratos"
            contratos = conector_banco_de_dados.conector_banco_de_dados(contratos_query).consultar()
            aditivos_query = "SELECT id_aditivos,detalhes FROM aditivos"
            aditivos = conector_banco_de_dados.conector_banco_de_dados(aditivos_query).consultar()
            return render_template("/produtos/criar_produto.html",
                                   contratos=contratos,
                                   aditivos=aditivos)
        
    def editar_produto(id_produto):
        lote = request.form["lote"]
        codigo = request.form["codigo"]
        descricao = request.form["descricao"]
        unidade = request.form["unidade"]
        quantidade_mensal = request.form["quantidade_mensal"]
        quantidade_anual = request.form["quantidade_anual"]
        valor_unitario = request.form["valor_unitario"]
        valor_total = request.form["valor_total"]
        id_contratos = request.form["id_contratos"]
        id_aditivos = request.form["id_aditivos"]
        if id_contratos != "" and id_aditivos != "":
            update_query = f"""
                UPDATE produtos
                SET lote = '{lote}', codigo = '{codigo}', descricao = '{descricao}', unidade = '{unidade}', quantidade_mensal = '{quantidade_mensal}', quantidade_anual = '{quantidade_anual}',
                valor_unitario = '{valor_unitario}', valor_total = '{valor_total}', id_contratos = '{id_contratos}', id_aditivos = '{id_aditivos}'
                WHERE id_produtos = '{id_produto}'
            """
            
        if id_aditivos == "" and id_contratos != "": 
            update_query = f"""
                UPDATE produtos
                SET lote = '{lote}', codigo = '{codigo}', descricao = '{descricao}', unidade = '{unidade}', quantidade_mensal = '{quantidade_mensal}', quantidade_anual = '{quantidade_anual}',
                valor_unitario = '{valor_unitario}', valor_total = '{valor_total}', id_contratos = '{id_contratos}'
                WHERE id_produtos = '{id_produto}'
            """
            
        if id_contratos == "" and id_aditivos == "":
            update_query = f"""
                UPDATE produtos
                SET lote = '{lote}', codigo = '{codigo}', descricao = '{descricao}', unidade = '{unidade}', quantidade_mensal = '{quantidade_mensal}', quantidade_anual = '{quantidade_anual}',
                valor_unitario = '{valor_unitario}', valor_total = '{valor_total}'
                WHERE id_produtos = '{id_produto}'
            """
        
        conector_banco_de_dados.conector_banco_de_dados(update_query).alterar_incluir_excluir()
        return redirect(url_for('produtos'))
    
    def obter_produto(id_produto):
        if request.method == 'GET':
            produto = conector_banco_de_dados.conector_banco_de_dados(f"SELECT * FROM produtos WHERE id_produtos = {id_produto}").consultar()
            if produto:
                produto = produto[0]
                produto_dict = {
                    'lote': produto[1],
                    'codigo': produto[2],
                    'descricao': produto[3],
                    'unidade': produto[4],
                    'quantidade_mensal': produto[5],
                    'quantidade_anual': produto[6],
                    'valor_unitario': produto[7],
                    'valor_total': produto[8],
                    'id_contratos': produto[9],
                    'id_aditivos': produto[10]
                }
                return render_template('produtos/editar_produto.html', produto=produto_dict)
    
    def excluir_produto(id_produto):
        delete_query = f"DELETE FROM produtos WHERE id_produtos = {id_produto}"
        conector_banco_de_dados.conector_banco_de_dados(delete_query).alterar_incluir_excluir()
        return redirect(url_for('produtos'))