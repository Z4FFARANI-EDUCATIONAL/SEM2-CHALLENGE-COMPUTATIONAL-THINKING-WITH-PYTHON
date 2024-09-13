# exemplos para consulta (filtro) de dados:
# consulta_produto = df[df['Produto'] == 'Mouse']

# ----------------------------------------

# Adiciona valores a uma lista:
# lista_produto_preco = df[['Produto', 'Preço']].values.tolist()

# ----------------------------------------

# Adicionar uma nova coluna calculada:
# df['Valor Total'] = df['Preço'] * df['Estoque']
# print(df)

# ----------------------------------------

# Agrupar produtos por categoria (exemplo de categorias fictícias)
# df['Categoria'] = ['Eletrônicos', 'Acessórios', 'Acessórios', 'Eletrônicos', 'Impressoras']
# Sumarizar o total da lista estoque por categoria
# estoque_por_categoria = df.groupby('Categoria')['Estoque'].sum()

# ----------------------------------------

# Lista de listas representando linhas de dados
# dados = [
#     ['Notebook', 3000, 5],
#     ['Teclado', 150, 25],
#     ['Mouse', 100, 30],
#     ['Monitor', 1200, 10],
#     ['Impressora', 800, 8]
# ]
# Criando o DataFrame
# df = pd.DataFrame(dados, columns=['Produto', 'Preço', 'Estoque'])
# print(df)

# ----------------------------------------

# import pandas as pd
# Criando um DataFrame de exemplo
# dados = {
#     'Categoria': ['Eletrônicos', 'Eletrônicos', 'Acessórios', 'Acessórios', 'Impressoras'],
#     'Produto': ['Notebook', 'Monitor', 'Teclado', 'Mouse', 'Impressora'],
#     'Preço': [3000, 1200, 150, 100, 800],
#     'Quantidade': [5, 10, 25, 30, 8]
# }
# df = pd.DataFrame(dados)
# Agrupar por 'Categoria' e somar o total de vendas
# df['Total de Vendas'] = df['Preço'] * df['Quantidade']
# vendas_por_categoria = df.groupby('Categoria')['Total de Vendas'].sum()
# print(vendas_por_categoria)

# ----------------------------------------

# Soma (sum): Soma todos os valores de cada grupo.
# Média (mean): Calcula a média dos valores de cada grupo.
# Contagem (count): Conta quantas entradas existem em cada grupo.
# Máximo/Mínimo (max, min): Encontra o valor máximo ou mínimo em cada grupo.

# ----------------------------------------

# corridas = {
#     'Fórmula 1': {
#         'combustivel': 'Gasolina',
#         'tipo_de_gasolina': 'Premium',
#         'ano': 2024
#     },
#     'Rali': {
#         'combustivel': 'Diesel',
#         'tipo_de_gasolina': 'Não aplicável',
#         'ano': 2023
#     },
#     'Stock Car': {
#         'combustivel': 'Gasolina',
#         'tipo_de_gasolina': 'Comum',
#         'ano': 2022
#     }
# }
# Convertendo o dicionário para DataFrame
# df = pd.DataFrame.from_dict(corridas, orient='index')

# Adicionando uma nova modalidade ao DataFrame
# nova_modalidade = pd.DataFrame({
#     'combustivel': ['Elétrico'],
#     'tipo_de_gasolina': ['Não aplicável'],
#     'ano': [2024]
# }, index=['Fórmula E'])

# df = pd.concat([df, nova_modalidade])

# ----------------------------------------

# Filtragem (df[df['coluna'] == valor]): Cria um novo DataFrame contendo apenas as linhas que atendem à condição. Não altera o DataFrame original, apenas permite visualizar ou analisar um subconjunto dos dados.
# Atualização (df.loc[]): Modifica diretamente o DataFrame original. É ideal para atualizar valores específicos em células do DataFrame.

# ----------------------------------------

# lambda
# funções
# loops (for e while)
# condições (if else)
# dataframes

# COMPARATIVO DE PERFORMANCE GERAL DE CARROS DE FÓRMULA:
    # Carros Avaliados: Fórmula 1, Fórmula 2, Fórmula 3, Fórmula 4, Fórmula E, Indy.
    # Critérios de Avaliação:
        # Combustível: Tipo e eficiência do combustível utilizado por cada carro.
        # Peso: Peso dos carros.
        # Aerodinâmica: Desempenho aerodinâmico de cada carro.
        # Valor Gasto: Custo associado ao uso e manutenção de cada carro.
        # Pista: Desempenho em um catálogo de 25 pistas diferentes.
    # Tempo de Corrida:
        # Média de Tempo: Calcular a média aritmética do tempo total que cada carro leva para completar 25 percursos, incluindo o tempo de PitStop.

# SISTEMA DE PONTUAÇÃO DE BLITZ:
    # Interação do Usuário: Implementar um sistema onde o usuário ganha pontos conforme interage com o código.
    # Explicação da Pontuação: Fornecer uma seção que explica como os pontos são obtidos e quais são suas utilidades.

# PROBABILÍSTICA PARA APOSTAS:
    # Base para Análise de Probabilidades: Desenvolver uma seção que calcula probabilidades para apostas baseadas nas pistas e desempenhos das escuderias.
    # Referência a E-Prix: Considerar desempenhos anteriores em E-Prix para ajustar as probabilidades de apostas.


import pandas as pd

corridas = {
    'Fórmula 1': {
        'combustivel': 'Gasolina',
        'tipo_de_gasolina': 'Premium',
        'ano': 2024
    },
    'Rali': {
        'combustivel': 'Diesel',
        'tipo_de_gasolina': 'Não aplicável',
        'ano': 2023
    },
    'Stock Car': {
        'combustivel': 'Gasolina',
        'tipo_de_gasolina': 'Comum',
        'ano': 2022
    }
}

# Convertendo o dicionário para DataFrame
df = pd.DataFrame.from_dict(corridas, orient='index')

print(df)