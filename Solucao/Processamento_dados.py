import pandas as pd #mapipulação de tabelas
import  glob as gb #localizar arquivos
import os #intergir com o sistema operacional(windows)
from Commons.Commons import DICIONARIO_PARA_PRODUTOS, NOMES_FILIAIS

def consolidar_vendas(mapa_precos):
    """
    :param mapa_precos:
    :return: df_final[colunas_finais]: dataframe do csv final anexando todas as filiais

    Lê todos os csv's das filiais e normaliza em um arquivo só
    """

    lista_dfs = [] #lista vazia de aquivos a serem manipulados

    origem = os.path.dirname(os.path.abspath(__file__))
    origem_dados = os.path.join(origem, "Commons")
    caminho_busca = os.path.join(origem_dados, "vendas_F*.csv")


    filial_arquivos = gb.glob(caminho_busca) #procurando por arquivos de vendas

    if not filial_arquivos:
        print(f"Aviso: Nenhum arquivo encontrado em {caminho_busca}. Verifique a pasta!")
        return None

    for arquivo in filial_arquivos:
        filial_id = arquivo.split("_")[2]#extraindo o nome(ex: F003)


        df = pd.read_csv(arquivo) #leitura do csv
        df['filial_id'] = filial_id
        df['filial_nome'] = NOMES_FILIAIS.get(filial_id, "Desconhecido")

        #Normalização das tabelas [EX: Quando produto for 'GC' vai ser traduzido para 'Gasolina Comum']
        df['produto_canonico'] = df['produto'].replace(DICIONARIO_PARA_PRODUTOS)

        #Calculando o volume (Valor/preço de referencia)
        df['preco_ref'] = df['produto_canonico'].map(mapa_precos)
        df['volume_estimado_litros'] = df['valor_total_brl']/df['preco_ref']

        lista_dfs.append(df)

    if not lista_dfs:
        return pd.DataFrame()

    df_final = pd.concat(lista_dfs, ignore_index=True)

    #
    colunas_finais = [
        'data',
        'filial_id',
        'filial_nome',
        'produto_canonico',
        'valor_total_brl',
        'volume_estimado_litros']
    return df_final[colunas_finais]


"""def salvar_relatorio(df, diretorio_raiz):

    pasta_saida = os.path.join(diretorio_raiz, "Resultados")
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)
    caminho_final = os.path.join(pasta_saida, "vendas_consolidadas_marco2025.csv")

    df.to_csv(caminho_final, index=False, encoding='utf-8-sig') # 'utf-8-sig' ajuda o Excel a ler acentos
    if os.path.exists(caminho_final):
        print("Arquivo 'vendas_consolidadas_marco2025.csv' gerado com sucesso!")
        print(f"Arquivo salvo em: {os.path.abspath(caminho_final)}")
        print(df.head())
    else:
        print("Nenhum arquivo de vendas  encontrado =/ ")"""

