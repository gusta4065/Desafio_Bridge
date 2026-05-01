# Mapeamento de IDs para Nomes de Filiais
NOMES_FILIAIS = {
    'F001': 'Posto Bandeirantes',
    'F002': 'Auto Posto Central',
    'F003': 'Posto São João',
    'F004': 'Ipiranga Express',
    'F005': 'Posto Litoral Norte'
}

# Mapeamento de variações para nomes oficiais (Nomes Canônicos)
DICIONARIO_PARA_PRODUTOS = {
    # Variações para Gasolina Comum
    'GC': 'Gasolina Comum',
    'Gas. Comum': 'Gasolina Comum',
    'Gasolina': 'Gasolina Comum',
    'Gasolina Comun': 'Gasolina Comum',
    'Gasolina C': 'Gasolina Comum',
    'Gasolina Comum': 'Gasolina Comum',

    # Variações para Etanol
    'Etanol Hidratado': 'Etanol',
    'Etanol Hid.': 'Etanol',
    'Etanol Comum': 'Etanol',
    'Alc.': 'Etanol',
    'Etanol': 'Etanol',

    # Variações para Diesel S10
    'DSL S10': 'Diesel S10',
    'Diesel': 'Diesel S10',
    'S10': 'Diesel S10',
    'Diesel S-10': 'Diesel S10',
    'Diesel S10 Aditivado': 'Diesel S10',
    'Diesel S10': 'Diesel S10',
}

# Colunas esperadas nos arquivos originais
COLUNAS_ORIGINAIS = ['data', 'produto', 'valor_total_brl']