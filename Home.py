import json
from Blitz import carregar_blitz, salvar_blitz
from IPF import *
from Probabilistica import *


arquivo_blitz = 'Blitz.json'  

while True:
    blitz = carregar_blitz(arquivo_blitz)   
    pergunta = int(input(f'''
Bem-vindo(a) ao Formula E•mmersive!

⚡ Blitz: {blitz} | Digite o número de uma das opções:

• Índice de Performance de Fórmula (IPF) [1]
• Probabilística (Aposte!) [2]
• Como os Blitz funcionam? [3]
• Encerrar [0]

>> '''))
    match pergunta:
        case 0:
            exit()
        case 1:
            blitz += 1000
            salvar_blitz(arquivo_blitz, blitz)
            while True:
                try:
                    modalidade = int(input(f'''
⚡ Blitz: {blitz} | Selecione a modalidade que deseja:

• Fórmula 1 [1]
• Fórmula 2 [2]
• Fórmula 3 [3]
• Fórmula E [4]
• Fórmula Indy [5]

>> '''))
                    if modalidade == 0:
                        exit()
                    elif modalidade in [1, 2, 3]:
                        blitz += 500
                        salvar_blitz(arquivo_blitz, blitz)
                        selecionado = f'formula{modalidade}'
                        break
                    elif modalidade == 4:
                        blitz += 1000
                        salvar_blitz(arquivo_blitz, blitz)
                        selecionado = 'formulaE'
                        break
                    elif modalidade == 5:
                        blitz += 1000
                        salvar_blitz(arquivo_blitz, blitz)
                        selecionado = 'formulaindy'
                        break
                    else:
                        print('Resposta inválida. Tente novamente.')
                except ValueError:
                    print('Entrada inválida. Por favor, digite um número.')

            print(IPF(selecionado, arquivo_blitz, blitz))

        case 2:
            while True:
                try:
                    if blitz >= 10000:
                        escuderia = int(input(f'''
⚡ Blitz: {blitz} | Aposte na escuderia de Fórmula E:

• Mahindra Racing [1]
• DS Techeetah [2]
• Audi Sport ABT Schaeffler [3]
• Nissan e.Dams [4]
• Jaguar Racing [5]
• Envision Virgin Racing [6]
• Mercedes-Benz EQ [7]
• Porsche Formula E [8]
• Dragon/Penske Autosport [9]
• Venturi Racing [10]

>> '''))
                        if escuderia == 0:
                                exit()
                        elif escuderia in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
                            selecionado = escuderia - 1
                            print(Probabilistica(selecionado, arquivo_blitz, blitz))
                            break
                        else:
                            print('Resposta inválida. Tente novamente.')
                    else:
                        print('Mínimo: ⚡ Blitz: 10.000 | Blitz insuficientes.')
                        break
                except ValueError:
                    print('Entrada inválida. Por favor, digite um número.')
        case 3:
            blitz += 1000
            salvar_blitz(arquivo_blitz, blitz)
            print(f'''
⚡ Blitz: {blitz} <---

O Blitz Point (ou apenas ⚡ Blitz) é uma pontuação dedicada ao Formula E•mmersive
que favorece o usuário a adquirir mais conhecimento sobre Fórmula e a participar de
apostas na seção Probabilística [2], trazendo imersão e divertimento para o sistema!''')

        case _:
            print('Resposta inválida. Tente novamente.')

    while True:
        try:
            continuar = int(input(f'''
• Continuar [1]
• Encerrar [0]

>> '''))
            if continuar == 0:
                print('''
Saindo... Até logo!''')
                exit()
            elif continuar == 1:
                break
            else:
                print('Opção inválida. Tente novamente.')
        except ValueError:
            print('Entrada inválida. Por favor, digite um número.')