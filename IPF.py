import pandas as pd
import json
from Blitz import salvar_blitz

with open('SEM2-CHALLENGE-COMPUTATIONAL-THINKING-WITH-PYTHON\data\IPF.json', 'r') as file:
    dados = json.load(file)


def IPF(selecionado, arquivo_blitz, blitz):
    circuito = pd.DataFrame(dados['circuito'][selecionado])
    velocidade_media = circuito['velocidade_media'].mean()
    EFcombustivel = pd.Series(dados['efc'][selecionado]).iloc[0]
    peso_modalidade = pd.Series(dados['peso'][selecionado]).iloc[0]
    peso_media = pd.DataFrame.from_dict(dados['peso']).mean(axis=1).iloc[0]
    Fpeso = 1 + (peso_modalidade / peso_media)

    print(f'''
⚡ Blitz: {blitz} | Selecione o circuito que deseja:
''')

    for i in range(len(circuito['nome'])):
        print(f'• {circuito["nome"][i]} [{i + 1}]')
    
    while True:
        try:
            pista = int(input('''
>> '''))
            if pista == 0:
                exit()
            elif 1 <= pista <= len(circuito):
                blitz += 300
                salvar_blitz(arquivo_blitz, blitz)
                break
            else:
                print('Resposta inválida. Tente novamente.')
        except ValueError:
            print('Entrada inválida. Por favor, digite um número.')

    comprimento_circuito = circuito.loc[pista - 1, 'comprimento']
    Tvolta = comprimento_circuito / velocidade_media * 60
        
    while True:
        try:
            clima = int(input(f'''
⚡ Blitz: {blitz} | Selecione o clima:

• Seco [1]
• Chuvoso [2]
• Extremo [3]

>> '''))
            match clima:
                case 0:
                    exit()
                case 1:
                    blitz += 100
                    salvar_blitz(arquivo_blitz, blitz)
                    Fclima = pd.Series(dados['clima']['seco']).iloc[0]
                    break
                case 2:
                    blitz += 100
                    salvar_blitz(arquivo_blitz, blitz)
                    Fclima = pd.Series(dados['clima']['chuvoso']).iloc[0]
                    break
                case 3:
                    blitz += 100
                    salvar_blitz(arquivo_blitz, blitz)
                    Fclima = pd.Series(dados['clima']['extremo']).iloc[0]
                    break
                case _:
                    print('Resposta inválida. Tente novamente.')
        except ValueError:
            print('Entrada inválida. Por favor, digite um número.')

    while True:
        try:
            pneu = int(input(f'''
⚡ Blitz: {blitz} | Selecione o tipo de pneu a ser utilizado:

• Seco [1]
• Chuva [2]
• Intermediário [3]

>> '''))
            match pneu:
                case 0:
                    exit()
                case 1:
                    blitz += 90
                    salvar_blitz(arquivo_blitz, blitz)
                    Fpneu = pd.Series(dados['pneu']['seco']).iloc[0]
                    break
                case 2:
                    blitz += 90
                    salvar_blitz(arquivo_blitz, blitz)
                    Fpneu = pd.Series(dados['pneu']['chuva']).iloc[0]
                    break
                case 3:
                    blitz += 90
                    salvar_blitz(arquivo_blitz, blitz)
                    Fpneu = pd.Series(dados['pneu']['intermediario']).iloc[0]
                    break
                case _:
                    print('Resposta inválida. Tente novamente.')
        except ValueError:
            print('Entrada inválida. Por favor, digite um número.')

    salvar_blitz(arquivo_blitz, blitz)
    IPF = (Tvolta / EFcombustivel) * Fpeso * Fclima * Fpneu

    return f'''
O IPF é calculado com o tempo de volta no circuito,
dividido pela eficiência de combustível do veículo da modalidade,
multiplicado pelo peso do mesmo veículo, pela condição climática escolhida
e pelo tipo de pneu selecionado.

Índice de Performance de Fórmula (IPF) = {IPF:.3f}'''