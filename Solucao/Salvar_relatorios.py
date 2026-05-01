import os


def salvar_relatorio(df, diretorio_raiz, nome_arquivo):
    """
    Função genérica para salvar DataFrames na pasta 'Resultados'.
    :param df: O DataFrame (tabela) a ser salvo.
    :param diretorio_raiz: O caminho da pasta principal do projeto.
    :param nome_arquivo: O nome do arquivo CSV (ex: 'vendas.csv').
    """
    if df is None:
        print("ERRO AO GERAR ARQUIVO")
        return

    # 1. Define e cria a pasta de saída de forma absoluta
    pasta_saida = os.path.join(diretorio_raiz, "Resultados")
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    # 2. Monta o caminho final com o nome dinâmico
    caminho_final = os.path.join(pasta_saida, nome_arquivo)

    # 3. Salva o arquivo
    # utf-8-sig garante compatibilidade de acentos com o Excel
    df.to_csv(caminho_final, index=False, encoding='utf-8-sig')

    # 4. Verificação e Feedback
    if os.path.exists(caminho_final):
        print(f"\n✓ Arquivo '{nome_arquivo}' gerado com sucesso!")
        print(f"Caminho: {os.path.abspath(caminho_final)}")
    else:
        print(f"× Erro ao gerar o arquivo '{nome_arquivo}'.")