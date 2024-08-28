import math
import os



def clear(): #funcão para realizar o apagamento das informações anteriores, com objetivo de deixar limpa a tela caso o usuario queira se manter no while reultilizando o programa
    os.system('cls' if os.name == 'nt' else 'clear')

def RecuperacaoEletricidade(DistanciaTotal): #função para calcular energia recuperada pelo carro eletrico que sera reultilizada
    
    EnergiaRecuperavel_perKM = 0.2
    consumo_energia_perKM = 0.67
    eficiencia = 0.70
    recuperaEnergia = EnergiaRecuperavel_perKM * DistanciaTotal * eficiencia
    gastoTotal = (consumo_energia_perKM * DistanciaTotal) - recuperaEnergia
    

    return gastoTotal

#calculos do mpg (milhas por galão) para descobrir a efiencia de cada carro em consumir seu tipo de energia designado

def mpg_eletrico(gastoTotal):

    CalcMPG = (33.7/gastoTotal) * 100

    return round(CalcMPG)

def mpg_gasolina(DistanciaTotal):
    
    consumo_Gasolina_perKM = 3

    Consumo_em_mpg = (consumo_Gasolina_perKM * 0.264172)/0.621371

    conversaoMilhas = DistanciaTotal * 0.621371
    
    mpg = conversaoMilhas/Consumo_em_mpg
    
    return mpg
#calculo de poluição apenas para o carro de gasolina devido ao fato do eletrico não produzir gases poluentes
def poluicao(DistanciaTotal):
    Co2Emitido_gramas = DistanciaTotal * 1500
    return Co2Emitido_gramas
#calculos do custo energetico baseado na cotação atual do preço de cada fonte
def custo_gas(DistanciaTotal):
    percorrer = DistanciaTotal * 10
    preco = percorrer * 5.85
    return round(preco, 2)

def custo_elec(DistanciaTotal):
    percorrer = DistanciaTotal * 0.2
    preco = percorrer * 0.656
    return round(preco, 2)
#função onde sera executado as outras funcoes do programa e onde ocorrera interação do usuario
def main():
    print('Bom dia, bem vindo ao comparador de carros de circuitos da formula-e e da formula 1, para iniciar por favor insira o tamanho do percurso onde sera realizada a comparação:')
    try:
        tamanhoPista = float(input('Digite Tamanho da pista (em km) ex 2.933 km: \n>'))
        velocidade_media = float(input("Digite a velocidade média do corredor (em km/h) ex: 121.23 km/h:\n>"))  
    except ValueError:
        print('Escolha inválida, Reinsira os valores númericos.')
        return
    
    print(f'Dado a velocidade média de {velocidade_media} e o tamanho da pista de {tamanhoPista}, informaremos a diferenca de MPG (Milhas por galão) entre os carros, a diferença de emissão de gases poluentes e a diferença de custo em dinheiro dos para os carros poderem percorrer o percurso proposto:\n')
    #informações base que serão usadas nas funções
    TempoTotal_min = 45  #Tempo limite de uma corrida de formula-e
    tempo_hora = TempoTotal_min / 60
    distancia45 = velocidade_media * tempo_hora  
    DistanciaTotal = distancia45 + tamanhoPista     

    gastoTotal = RecuperacaoEletricidade(DistanciaTotal)
    mpgElect = mpg_eletrico(gastoTotal)
    mpgGAS = mpg_gasolina(DistanciaTotal)
    
    mpgDiff = mpgElect - mpgGAS
    if mpgDiff > 0:
        mpg_porcentagem = round(((mpgGAS / mpgElect) * 100))
        print(f'O carro eletrico é mais eficiente por {mpgDiff} MPG (milhas por galão), tornando o carro eletrico {mpg_porcentagem}% mais eficiente em gasto de energia\n')
    else: 
        mpg_porcentagem = ((mpgElect / mpgGAS) * 100)
        print(f'O MPG do carro à Gás é mais eficiente por {mpgDiff * (-1)}, tornando o carro à Gás {mpg_porcentagem}% mais eficiente em gasto de energia\n')

    poluicao_gasolina = poluicao(DistanciaTotal)
    print(f'A emissão de CO2 do carro de formula 1 é de {poluicao_gasolina:.2f} gramas. Por conta do carro da Formula-E ser eletrico ele nao emite gases poluentes\n')

    preco_elect = custo_elec(DistanciaTotal)
    preco_gas = custo_gas(DistanciaTotal)


    print(f'O custo para o carro à gasolina percorrer {DistanciaTotal} km é de R$ {preco_gas}.')
    print(f'O custo para o carro elétrico percorrer {DistanciaTotal} km é de R$ {preco_elect}.\n')

    input('Pressione Enter para voltar ao menu')
#Uso do while para permitir que o usuario possa realizar diversas vezes o programa
while True:
    clear()
    escolha = input('Deseja realizar a comparação entre um carro de Formula-E e um carro de Formula 1? (s/n): ').upper()
    if escolha == 'S':
        main()
    elif escolha == 'N':
        break
    else:
        print('Escolha inválida. Por favor, insira "s" para sim ou "n" para não.')