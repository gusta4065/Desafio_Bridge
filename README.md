# Desafio_Bridge

# ⛽ Sistema de Inteligência e Consolidação de Dados - Rede de Postos

Este projeto foi desenvolvido como solução para o desafio técnico da **Bridge & Co.**, focado na automação de coleta de preços, consolidação de vendas e análise de inteligência artificial para uma rede de postos de combustíveis.

## 🚀 Diferenciais Técnicos
- **RPA (Web Scraping)**: Coleta automatizada de preços de referência via site oficial usando `lxml` e `Pandas`.
- **Inteligência Artificial**: Integração com o modelo **Gemini 3 Flash Preview** para análise de sentimento e resumos executivos de relatos de gerentes.
- **Segurança**: Uso de variáveis de ambiente (`.env`) para proteção de chaves de API.
- **Arquitetura Profissional**: Estrutura modularizada separando lógica de negócio, componentes e utilitários.

---

## 📂 Estrutura do Projeto
O projeto utiliza uma organização baseada em padrões de mercado para facilitar a escalabilidade e manutenção:
```text
Desafio_Bridge/
├── data/
│   └── raw/               # Dados brutos (CSVs e TXTs das filiais)
├── src/                   # Código-fonte principal
│   ├── output/            # Resultados finais processados
│   ├── components/        # Integração com IA (Gemini) e Coletor (RPA)
│   ├── processing/        # Lógica de consolidação e tratamento de dados
│   ├── utils/             # Funções auxiliares (Helpers)
│   └── main.py            # Ponto de entrada (Orquestrador)
└── .env                   # Configurações sensíveis (não incluído no Git)
```

🛠️ Tecnologias Utilizadas
Python 3.12+

Pandas: Manipulação de dados e leitura de HTML.

Google GenAI SDK: Conexão com o modelo Gemini 3 Flash.

Python-dotenv: Gerenciamento de variáveis de ambiente.

Requests & LXML: Requisições web e parsing de dados.

---

### 📋 Pré-requisitos e Execução

Para garantir que todas as dependências (como `pandas` e o SDK do Gemini) sejam instaladas corretamente sem conflitos com o sistema operacional, recomendo o uso de um ambiente virtual.

<details>


#### 1. Clonar o repositório
```bash
git clone [URL_DO_REPOSITORIO]
cd Desafio_Bridge
```

#### 2. Configurar o Ambiente Virtual (Recomendado)
No terminal, execute os comandos abaixo de acordo com o seu sistema:

**Linux / macOS / Codespaces:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (PowerShell):**
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

#### 3. Instalar Dependências
Com o ambiente virtual ativo, instale os pacotes necessários:
```bash
pip install -r requirements.txt
```

#### 4. Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto e adicione sua chave da API do Google:
```text
GOOGLE_API_KEY=sua_chave_aqui
```

#### 5. Execução do Projeto
Para que o Python localize corretamente os módulos internos da pasta `src`, execute o comando a partir da raiz do projeto:

```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"
python3 src/Main.py
```
*(No Windows, utilize `set PYTHONPATH=%PYTHONPATH%;%cd%\src` antes de rodar o script).*

</details>

---
### 📚 Documentação das Funções


#### **1. buscar_precos_web**
*   **Pacote:** `src.components.coletor_precos`
*   **Parâmetros:** Nenhum.
*   **Retorno:** `dict` (Dicionário contendo os preços coletados por produto).
<details>
<summary><b>Explicação:</b></summary>
Realiza a coleta automatizada (RPA) de preços de referência no site oficial. Utiliza o `Pandas` para fazer o parsing de tabelas HTML e retorna os valores normalizados para uso no cálculo de volume.
</details>

#### **2. consolidar_vendas**
*   **Pacote:** `src.processing.processamento_dados`
*   **Parâmetros:** `mapa_precos` (dict).
*   **Retorno:** `pd.DataFrame` (Tabela consolidada com todas as filiais).
<details>
<summary><b>Explicação:</b></summary> Percorre a pasta de dados brutos, unifica os arquivos CSV de vendas de todas as filiais, aplica a normalização dos nomes dos produtos e calcula o volume estimado em litros com base nos preços reais coletados pelo RPA.
</details>

#### **3. analisar_email_gerentes**
*   **Pacote:** `src.components.analisador_ia`
*   **Parâmetros:** Nenhum.
*   **Retorno:** `None` (Gera o arquivo de saída diretamente).

<details>
<summary><b>Explicação:</b></summary>
Orquestra a leitura dos relatos em texto dos gerentes, envia os dados para a API do **Gemini 3 Flash Preview** e processa a resposta JSON para extrair o resumo, destaques, alertas e o sentimento geral de cada filial.

</details>

#### **4. salvar_relatorios**
*   **Pacote:** `src.utils.helpers.salvar_relatorios`
*   **Parâmetros:** `df` (pd.DataFrame), `nome_arquivo` (str).
*   **Retorno:** `None`.
<details>
<summary><b>Explicação:</b></summary>
Função utilitária responsável pela persistência de dados. Ela verifica a existência da pasta `output` na raiz do projeto, cria o diretório se necessário e salva o DataFrame em formato CSV com suporte a caracteres especiais (UTF-8-SIG).
</details>


---
### 📊 Resultados Gerados
Após a execução, os seguintes arquivos estarão disponíveis na pasta ```output/:```

- vendas_consolidadas_marco2025.csv: Dados de vendas unificados com cálculo de volume baseado nos preços reais coletados via RPA.

- resumo_gerentes_marco2025.csv: Análise estruturada (JSON para CSV) contendo resumo, alertas e sentimento geral extraídos por IA.

## 🚀 Próximos Passos & Evolução (Java Version)
Como parte do meu desenvolvimento contínuo como desenvolvedor, planejo recriar este projeto utilizando o ecossistema **Java**, explorando as seguintes melhorias:

- **Backend com Spring Boot**: Migração da lógica de processamento para uma arquitetura de microserviços.
- **Spring AI**: Integração nativa com modelos de linguagem (LLMs) utilizando as novas bibliotecas do ecossistema Spring.
- **OpenCSV / Apache POI**: Para um processamento de arquivos de alto desempenho e tipagem forte.
- **Containerização**: Empacotamento da aplicação com Docker para facilitar o deploy e a escalabilidade.


---

Desenvolvido por: Luiz Gustavo Lucio Pereira
Objetivo: Desafio Técnico Estágio Bridge & Co. 2026


---
