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
            query = f'''INSERT INTO produtos(lote,codigo,descricao,unidade,quantidade_mensal,quantidade_anual,valor_unitario,valor_total,id_contratos,id_aditivos)
                        VALUES ('{lote}','{codigo}','{descricao}','{unidade}','{quantidade_mensal}','{quantidade_anual}','{valor_unitario}','{valor_total}','{id_contratos}','{id_aditivos}')'''
            conector_banco_de_dados.conector_banco_de_dados(query).alterar_incluir_excluir()
            mensagem = "Produto adicionado!"
            return render_template("/produtos/criar_produto.html",
                                   mensagem = mensagem)

    def obter_formulario_produto():
        if request.method == "GET":
            return render_template("/produtos/criar_produto.html")