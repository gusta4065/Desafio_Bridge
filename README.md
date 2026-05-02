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
│   ├── components/        # Integração com IA (Gemini) e Coletor (RPA)
│   ├── processing/        # Lógica de consolidação e tratamento de dados
│   ├── utils/             # Funções auxiliares (Helpers)
│   └── main.py            # Ponto de entrada (Orquestrador)
├── output/                # Resultados finais processados
└── .env                   # Configurações sensíveis (não incluído no Git)
```

🛠️ Tecnologias Utilizadas
Python 3.12+

Pandas: Manipulação de dados e leitura de HTML.

Google GenAI SDK: Conexão com o modelo Gemini 3 Flash.

Python-dotenv: Gerenciamento de variáveis de ambiente.

Requests & LXML: Requisições web e parsing de dados.

⚙️ Como Executar
1. Pré-requisitos
Certifique-se de ter o Python instalado. Recomenda-se o uso de um ambiente virtual (venv).

2. Instalação das Dependências
No terminal, instale os pacotes necessários:

```Bash
pip install pandas google-genai python-dotenv requests lxml
```

3. Configuração da API
Crie um arquivo .env na pasta src/ (ou na raiz, conforme sua configuração) com a sua chave do Google AI Studio:

```Plaintext
GEMINI_API_KEY=SUA_CHAVE_AQUI
```
4. Execução
Execute o script principal para processar todos os dados e gerar os relatórios:

```Bash
python src/main.py
```

📊 Resultados Gerados
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
