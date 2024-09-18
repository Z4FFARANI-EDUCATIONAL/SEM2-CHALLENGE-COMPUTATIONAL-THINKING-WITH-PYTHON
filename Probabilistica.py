import pandas as pd
import json
import random
from Blitz import salvar_blitz

with open('SEM2-CHALLENGE-COMPUTATIONAL-THINKING-WITH-PYTHON\data\Probabilistica.json', 'r') as file:
    dados = json.load(file)


def Probabilistica(selecionado, arquivo_blitz, blitz):
    escuderia = dados['escuderias'][selecionado]
    escuderia_df = pd.DataFrame([escuderia])

    NVT = escuderia_df['vitorias'].values[0]
    NTC = 116
    fator_circuito = 0
    fator_clima = 0
    fator_posicao = 0
    multiplicador = 0

    print(f'''
⚡ Blitz: {blitz} | Selecione o circuito que deseja:
''')

    for i, circuito in enumerate(dados['escuderias'], start=1):
        print(f'• {circuito["fator_circuito"]} [{i}]')

    while True:
        try:
            circuito = int(input('''
>> '''))
            if circuito == 0:
                exit()
            elif circuito == escuderia['numero_circuito']:
                fator_circuito += 2
                break
            elif circuito in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
                break
            else:
                print('Resposta inválida. Tente novamente.')

        except (ValueError, IndexError):
            print('Resposta inválida. Tente novamente.')

    clima = random.choice([1, 2])

    if clima == escuderia['numero_clima']:
        fator_clima += 2
    elif clima in [1, 2]:
        pass

    posicao_fatores = {
        1: 1.00,
        2: 0.95,
        3: 0.90,
        4: 0.85,
        5: 0.80,
        6: 0.75,
        7: 0.70,
        8: 0.65,
        9: 0.60,
        10: 0.55,
        11: 0.50,
        12: 0.45,
        13: 0.40,
        14: 0.35,
        15: 0.30,
        16: 0.25,
        17: 0.20,
        18: 0.15,
        19: 0.10,
        20: 0.05,
        21: 0.05,
        22: 0.05
    }

    posicao_aleatoria = random.choice(list(posicao_fatores.keys()))
    fator_posicao = posicao_fatores[posicao_aleatoria]

    while True:
        try:
            aposta = int(input(f'''
Quanto deseja apostar? 

⚡ Blitz: {blitz}

>> '''))
            if aposta > blitz:
                print('Saldo insuficiente. Tente novamente.')
            else:
                while True:
                    try:
                        certeza = int(input(f'''             
⚡ Blitz: {blitz} | Confirmar aposta?

♦ Sua aposta: {aposta}

• Sim [1]
• Não [2]

>> '''))
                        if certeza == 1:
                            blitz -= aposta
                            salvar_blitz(arquivo_blitz, blitz)
                            if aposta >= 500000:
                                multiplicador = 2.00
                            elif aposta >= 100000:
                                multiplicador = 1.85
                            elif aposta >= 50000:
                                multiplicador = 1.70
                            elif aposta >= 10000:
                                multiplicador = 1.55
                            elif aposta >= 5000:
                                multiplicador = 1.40
                            elif aposta >= 1000:
                                multiplicador = 1.25
                            else:
                                multiplicador = 1.10
                            break
                        elif certeza == 2:
                            return 'Aposta cancelada.'
                        else:
                            print('Resposta inválida. Tente novamente.')
                    except ValueError:
                        print('Entrada inválida. Por favor, digite um número.')
                break
        except ValueError:
            print('Entrada inválida. Por favor, digite um número.')

    Fajuste = fator_circuito + fator_clima + fator_posicao
    PV = NVT / NTC * Fajuste * multiplicador

    if PV >= 2.00:
        blitz += 1000000
        salvar_blitz(arquivo_blitz, blitz)
        return f'''
Lendário! Sua escuderia conquistou o 1º lugar e ganhou o campeonato mundial!

⚡ Blitz: 1.000.000 foram adicionados à sua conta.'''
    elif PV >= 1.50:
        blitz += 500000
        salvar_blitz(arquivo_blitz, blitz)
        return f'''
Parabéns! Sua escuderia alcançou o 2º lugar e ganhou muitos patrocínios.

⚡ Blitz: 500.000 foram adicionados à sua conta.'''
    elif PV >= 1.00:
        blitz += 250000
        salvar_blitz(arquivo_blitz, blitz)
        return f'''
Muito bem! Sua escuderia chegou em 3º lugar e repercutiu nas mídias.

⚡ Blitz: 250.000 foram adicionados à sua conta.'''
    elif PV >= 0.80:
        blitz += 100000
        salvar_blitz(arquivo_blitz, blitz)
        return f'''
Ótima corrida! Sua escuderia ficou em 4º lugar e chamou a atenção.

⚡ Blitz: 100.000 foram adicionados à sua conta.'''
    elif PV >= 0.60:
        blitz += 50000
        salvar_blitz(arquivo_blitz, blitz)
        return f'''
Persista! Sua escuderia ficou em 5º lugar e se classificou.

⚡ Blitz: 50.000 foram adicionados à sua conta.'''
    elif PV >= 0.40:
        blitz += 25000
        salvar_blitz(arquivo_blitz, blitz)
        return f'''
Valeu! Sua escuderia ficou em 6º lugar e se classificou.

⚡ Blitz: 25.000 foram adicionados à sua conta.'''
    elif PV >= 0.20:
        blitz += 10000
        salvar_blitz(arquivo_blitz, blitz)
        return f'''
Boa! Sua escuderia ficou em 7º lugar e se classificou.

⚡ Blitz: 10.000 foram adicionados à sua conta.'''
    else:
        return f'''
Infelizmente, sua escuderia não se classificou.

⚡ Blitz: Nenhuma quantia foi adicionada à sua conta.'''