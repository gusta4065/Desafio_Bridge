import requests
import pandas as pd
from io import StringIO

def Busca_precos_web():
    """
    Realiza a coleta dutomatica dos precos via web

    retorna um dicionário com os precos atualizados
    """
    url = "https://bridgenoc.github.io/case-postos/precos_marco2025.html"

    try:
        # 1. Faz a requisição HTTP automática
        print(f"Acessando: {url}")
        resposta = requests.get(url)
        resposta.raise_for_status() # Garante que o site está online

        # 2. Extrai a tabela do HTML
        # uso do StringIO para que o Pandas entenda o texto como um arquivo
        html_puro = StringIO(resposta.text)
        tabelas = pd.read_html(html_puro, flavor="lxml")

        # Pegamos a primeira tabela encontrada na página
        df_precos = tabelas[0]

        # 3. Transforma em um dicionário para o cálculo de volume
        # Ex: {'Gasolina Comum': 5.75, 'Etanol': 3.89, ...}
        mapa_precos = dict(zip(df_precos['produto'], df_precos['preco_medio_litro_brl']))

        print("✓ Preços de referência coletados com sucesso via RPA.")
        return mapa_precos

    except Exception as e:
        print(f"× Erro na coleta via web: {e}")
        return None

