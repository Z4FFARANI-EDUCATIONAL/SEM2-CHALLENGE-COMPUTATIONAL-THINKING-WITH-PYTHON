![banner](./assets/banner.png)

# INTEGRANTES:
- **Guilherme Santos Nunes** | 558989
- **Kaique Rodrigues Zaffarani** | 556677
- **Kairo da Silva Silvestre de Carvalho** | 558288
- **Rafael Menezes Viana** | 558287

## LINKS
- **[VÍDEO EXPLICATIVO](https://youtu.be/TjPJysby_Hc)**

<br>

# PROJETO
A **[Tech Mahindra](https://www.techmahindra.com)**, em parceria com a **[FIAP](https://www.fiap.com.br)**, busca popularizar a Fórmula E por meio de soluções tecnológicas práticas e interativas. Portanto, este projeto é uma simulação interativa que permite ao usuário explorar o mundo da Fórmula E de maneira imersiva. O usuário pode calcular o Índice de Performance de Fórmula (IPF) para diversas modalidades de corridas, além de apostar em escuderias no modo probabilístico, usando os Blitz Points como moeda interna do sistema.

O programa é composto por três sistemas principais:

- **Índice de Performance de Fórmula (IPF)** | Permite ao usuário calcular o IPF baseado na modalidade de corrida selecionada.
- **Probabilística** | O usuário pode apostar nos resultados de corridas de Fórmula E, utilizando fatores como clima, circuito e posição, para determinar o vencedor.
- **Blitz** | O sistema de pontos que serve tanto como recompensa quanto como moeda para apostar.

<br>

# INSTRUÇÕES
No terminal, clonar o repositório copiando o endereço https://github.com/Z4FFARANI-EDUCATIONAL/SEM2-CHALLENGE-COMPUTATIONAL-THINKING-WITH-PYTHON.git.

Para rodar o programa, no terminal, executar o arquivo ```Home.py``` exibirá um menu interativo onde o usuário poderá escolher entre calcular o IPF, fazer apostas ou visualizar o funcionamento dos Blitz Points.

Após selecionar a opção IPF, o usuário pode escolher entre cinco diferentes modalidades de corrida: Fórmula 1, Fórmula 2, Fórmula 3, Fórmula E e Fórmula Indy. O sistema incrementa os Blitz a cada cálculo realizado.

No modo de apostas, o usuário pode apostar na performance de escuderias de Fórmula E. Baseado em fatores como o circuito, clima e posição, o resultado da aposta pode gerar recompensas variáveis, podendo chegar a 1.000.000 de Blitz. O mínimo de Blitz para começar a apostar é de 10.000.

Os Blitz Points são acumulados ao interagir com o sistema. O sistema detalha como esses pontos são utilizados e acumulados ao selecionar a opção correspondente no menu.

<br>

# FUNÇÕES
``IPF.py``:
- **comprimento_circuito** | Comprimento do circuito escolhido pelo usuário em quilômetros, que é obtido de ``IPF.json``.
- **Tvolta = comprimento_circuito / velocidade_media * 60** | Cálculo de tempo de uma volta no circuito. Velocidade média, é do circuito, sendo resgatado em ``IPF.json``.
- **EFcombustivel** | Nível de eficiência do combustível dependendo da modalidade escolhida.
- **Fpeso** | Fator peso do veículo, presente em ``IPF.json``.
- **Fclima** | Fator clima do ambiente, presente em ``IPF.json``.
- **Fpneu** | Fator do tipo de pneu, presente em ``IPF.json``.
- **IPF = (Tvolta / EFcombustivel) * Fpeso * Fclima * Fpneu** | Cálculo de Índice de Performance de Fórmula.
  
<br>

``Probabilistica.py``:
- **NVT** | Número total de vitórias que a escuderia escolhida pelo usuário obteve.
- **NTC** | Número total de corridas realizadas durante toda a história da Fórmula E.
- **fator_circuito** | Fator de escolha do circuito pelo usuário presente em ``Probabilistica.json``. Caso o usuário acerte o circuito em que a escuderia tem melhor desempenho, a probabilidade de uma recompensa considerável é maior.
- **fator_clima** | Fator de condições climáticas presente em ``Probabilistica.json`` decidido aleatoriamente pelo sistema.
- **fator_posicao** | Fator de posição inicial para corrida simulada, decidido aleatoriamente pelo sistema.
- **Fajuste = fator_circuito + fator_clima + fator_posicao** | Cálculo de Fator de Ajuste.
- **multiplicador** | Código com condicional capaz de multiplicar a pontuação de resultado dependendo da quantidade de Blitz apostada.
- **PV = NVT / NTC * Fajuste * multiplicador** | Cálculo da Probabilidade de Vitória.

<br>

# FLUXOGRAMA
![fluxograma](./assets/fluxograma.png)

<br>

# OBSERVAÇÕES
- Alguns valores dispostos em arquivos não condizem com a realidade e apenas servem para fins educativos.
- A importação e estabelecimento de parâmetros em funções permitem conexão entre arquivos e bibliotecas.
- Textos que são exibidos durante a execução do programa estão fora de identação nos códigos para melhor visualização. 
- O arquivo ``Blitz.json`` é criado e utilizado para armazenar e carregar o saldo em Blitz do usuário por mais que o programa se encerre.
- O arquivo ``Probabilistica.py`` inclui um conjunto de dados em ``Probabilistica.json`` que contém informações sobre as escuderias de Fórmula E e fatores cruciais para apostas.

<br>

# TECNOLOGIAS
**[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/downloads/)**
**[![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/docs/getting_started/install.html)**

<br>

# REFERÊNCIAS
- **[Como funcionam as apostas esportivas?](https://www.lance.com.br/resenha-de-apostas/basico/como-funcionam-as-apostas-esportivas.html)**
- **[O que é probabilidade?](https://beduka.com/blog/materias/matematica/o-que-e-probabilidade/)**
- **[Circuitos de Fórmula 1](https://pt.wikipedia.org/wiki/Lista_de_autódromos_de_Fórmula_1)**
- **[Circuitos de Fórmula 2](https://pt.wikipedia.org/wiki/Campeonato_de_Fórmula_2_da_FIA)**
- **[Circuitos de Fórmula 3](https://pt.wikipedia.org/wiki/Campeonato_de_Fórmula_3_da_FIA)**
- **[Circuitos de Fórmula E](https://pt.wikipedia.org/wiki/Categoria:Circuitos_de_Fórmula_E)**
- **[Circuitos de Fórmula Indy](https://pt.wikipedia.org/wiki/Lista_de_circuitos_da_IndyCar_Series)**
