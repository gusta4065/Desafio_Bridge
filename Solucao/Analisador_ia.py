import os
import glob
import json
from http.client import responses

import pandas as pd
from google import genai
from dotenv import load_dotenv

#pegando a chave da api do .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("Erro: GEMINI_API_KEY não encontrada. Verifique seu arquivo .env.")
else:
    #indexado a chave
    client = genai.Client(api_key=API_KEY)
    print("✓ Chave de API carregada com segurança!")

def analisar_email_gerentes():
    """
    Lê os e-mails da pasta Commons e utiliza o Gemini para gerar um relatório estruturado.
    """

    #Busca os emails na pasta Commons igual acontece no arquivo 'Processamento_dados.py'
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_emails = os.path.join(diretorio_atual, "Commons", "email_F*.txt")
    emails = glob.glob(caminho_emails)

    lista_resultados = []

    if not emails:
        print("Nenhum arquivo de e-mail (.txt) encontrado na pasta Commons.")
        return
    for email_caminho in emails:
        nome_arquivo = os.path.basename(email_caminho)
        filial_id = nome_arquivo.split("_")[1]

        with open(email_caminho, 'r', encoding='utf-8') as f:
            texto_email = f.read()
        prompt = f"""
        Analise o e-mail do gerente abaixo e retorne APENAS um objeto JSON com os seguintes campos:
        - resumo: síntese do relato em 2 a 3 frases
        - destaques: lista de até 3 pontos relevantes mencionados
        - alertas: problemas ou ocorrências que merecem atenção da sede (se não houver, deixe vazio "")
        - sentimento_geral: escolha apenas entre (positivo | neutro | negativo)

        E-mail:
        {texto_email}
        """

        try:
            #chamada à API do Gemini
            response = client.models.generate_content(
                model="gemini-3-flash-preview",

                contents=prompt
            )

            #limpando marcações de markdown
            texto_limpo = response.text.strip()
            if "```json" in texto_limpo:
                texto_limpo = texto_limpo.split("```json")[1].split("```")[0].strip()
            elif "```" in texto_limpo:
                texto_limpo = texto_limpo.split("```")[1].split("```")[0].strip()

            dados = json.loads(texto_limpo)
            dados['filial_id'] = filial_id
            lista_resultados.append(dados)

            print(f"✓ Filial {filial_id} processada com sucesso.")
        except Exception as e:
            print(f"× Erro ao processar filial {filial_id}: {e}")

    if lista_resultados:
        df_ia = pd.DataFrame(lista_resultados)

        # Ordenando colunas conforme o PDF do desafio
        colunas_final = ['filial_id', 'resumo', 'alertas', 'sentimento_geral']
        return  df_ia[colunas_final]
    else:
        return pd.DataFrame()