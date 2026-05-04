import os.path

from components.Analisador_ia import analisar_email_gerentes
from processing.Processamento_dados import consolidar_vendas , gerar_ranking_desempenho
from utils.helpers.Salvar_relatorios import salvar_relatorio
from components.Coletor_precos import Busca_precos_web

##Dicionario de preco pra  Testes

"""precos_exemplo = {
    'Gasolina Comum': 5.80,
    'Etanol': 3.90,
    'Diesel S10': 6.10
}"""


def Main():
    print("Bem vindo a ferramenta de processamento de preços ")
    Diretorio_raiz = os.path.dirname(os.path.abspath(__file__))

    mapa_precos = Busca_precos_web()

    if mapa_precos is not None:
        print("✓ Preços carregados. Iniciando consolidação...")
        df_resultado= consolidar_vendas(mapa_precos)
        if df_resultado is not None:
            salvar_relatorio(df_resultado,Diretorio_raiz , 'vendas_consolidadas_marco2025.csv');
    else:
        print("× Não foi possível obter os preços de referência do site.")

    print(" Iniciando relatorio de gerentes")
    resumo_ia_df = analisar_email_gerentes()
    salvar_relatorio(resumo_ia_df,Diretorio_raiz, "resumo_gerentes_marco2025.csv")

    print("criando ranking das filiais")
    ranking_filiais, ranking_produtos = gerar_ranking_desempenho(df_resultado)
    salvar_relatorio(ranking_filiais,Diretorio_raiz, "ranking_filiais_marco2025.csv")
    salvar_relatorio(ranking_produtos,Diretorio_raiz, "ranking_produtos_marco2025.csv")



if __name__ == "__main__":
    Main()
