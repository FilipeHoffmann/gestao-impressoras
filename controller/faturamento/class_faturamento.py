from flask import render_template, request, url_for, redirect
from static.scripts import conector_banco_de_dados

class class_faturamento:
    @staticmethod
    def faturamento():
        query = f'''
        SELECT secretarias.nome, setores.nome_setor, impressoras.id_impressoras, cotas.tipo_cota,impressoras.status, c.data_coleta, c.paginas_impressas,cotas.cota_mensal,produtos.valor_unitario
        FROM contadores AS c
        INNER JOIN setores ON c.id_setores = setores.id_setores
        INNER JOIN secretarias ON setores.id_secretarias = secretarias.id_secretarias
        INNER JOIN impressoras ON c.id_impressoras = impressoras.id_impressoras
        INNER JOIN cotas ON impressoras.id_cotas = cotas.id_cotas
        INNER JOIN produtos ON produtos.id_produtos= c.id_produtos
        WHERE impressoras.status = "ATIVA" OR impressoras.status = "TROCADA"
        ORDER BY secretarias.nome ASC
        '''
        lista_contadores = conector_banco_de_dados.conector_banco_de_dados(query).consultar()
        custo_total = 0
        #Adicionando a coluna EXCEDENTES e TOTAL A PAGAR
        for i in range(len(lista_contadores)):
            lista_contadores[i] = list(lista_contadores[i])
            if (lista_contadores[i][6]-lista_contadores[i][7]) <= 0:
                lista_contadores[i].append(0)
                lista_contadores[i].append(0.0)
            else:
                lista_contadores[i].append(lista_contadores[i][6]-lista_contadores[i][7])
                lista_contadores[i].append(lista_contadores[i][8]*lista_contadores[i][9])
            custo_total += lista_contadores[i][10]
        return render_template("/faturamento/faturamento.html",
                               faturamentos = lista_contadores,
                               custo_total=custo_total)
    
    def obter_faturamento(mes):
        query = f'''
        SELECT secretarias.nome, setores.nome_setor, impressoras.id_impressoras, cotas.tipo_cota,impressoras.status, c.data_coleta, c.paginas_impressas,cotas.cota_mensal,produtos.valor_unitario
        FROM contadores AS c
        INNER JOIN setores ON c.id_setores = setores.id_setores
        INNER JOIN secretarias ON setores.id_secretarias = secretarias.id_secretarias
        INNER JOIN impressoras ON c.id_impressoras = impressoras.id_impressoras
        INNER JOIN cotas ON impressoras.id_cotas = cotas.id_cotas
        INNER JOIN produtos ON produtos.id_produtos= c.id_produtos
        WHERE c.mes_referente = "{mes}" AND (impressoras.status = "ATIVA" OR impressoras.status = "TROCADA")
        ORDER BY secretarias.nome ASC
        '''
        lista_contadores = conector_banco_de_dados.conector_banco_de_dados(query).consultar()
        custo_total = 0
        #Adicionando a coluna EXCEDENTES e TOTAL A PAGAR
        for i in range(len(lista_contadores)):
            lista_contadores[i] = list(lista_contadores[i])
            if (lista_contadores[i][6]-lista_contadores[i][7]) <= 0:
                lista_contadores[i].append(0)
                lista_contadores[i].append(0.0)
            else:
                lista_contadores[i].append(lista_contadores[i][6]-lista_contadores[i][7])
                lista_contadores[i].append(lista_contadores[i][8]*lista_contadores[i][9])
            custo_total += lista_contadores[i][10]
            
        return render_template("/faturamento/faturamento.html",
                               faturamentos = lista_contadores,
                               custo_total=custo_total,
                               mes=mes)
        