# PLC_21_22
Projetos realizados no âmbilo da cadeira de Processamento de Linguagens e Compiladores.

------------

TP1 - Processador de Inscritos numa atividade desportiva 

Enunciado: Construa agora um ou vários programas Python para processar o texto 'inscritos.txt' conforme solicitado nas alíneas seguintes: 

a) imprimir o nome e o email dos concorrentes inscritos entre a 5 e a 15 posições. 

b) imprimir o nome dos concorrentes que se inscrevem como 'Individuais' e são de 'Valongo'. 

c) imprimir o telemóvel e a prova em que está inscrito cada concorrente cujo nome seja 'Paulo' ou 'Ricardo', desde que seja da Vodafone. 

d) imprimir os 20 primeiros registos com os nomes convertidos para minúsculas. 

e) imprimir os 20 primeiros registos num novo ficheiro de output mas em formato Json.

-----------

TP2 - Definição uma linguagem de programação imperativa simples

Enunciado: Pretende-se que comece por deﬁnir uma linguagem de programação imperativa simples, a seu gosto.

Apenas deve ter em consideração ao que essa linguagem terá de permitir: 

• declarar variáveis atómicas do tipo inteiro, com os quais se podem realizar as habituais operações aritméticas, relacionais e lógicas.

• efetuar instruções algorítmicas básicas como a atribuição do valor de expressões numéricas a variáveis. 

• ler do standard input e escrever no standard output. 

• efetuar instruções condicionais para controlo do ﬂuxo de execução. 

• efetuar instruções cíclicas para controlo do ﬂuxo de execução, permitindo o seu aninhamento. 

Note que deve implementar pelo menos o ciclo while-do, repeat-until ou for-do. 

Adicionalmente deve ainda suportar, à sua escolha, uma das duas funcionalidades seguintes: 

• declarar e manusear variáveis estruturadas do tipo array (a 1 ou 2 dimensões) de inteiros, em relação aos quais é apenas permitida a operação de indexação (índice inteiro). 

• deﬁnir e invocar subprogramas sem parâmetros mas que possam retornar um resultado do tipo inteiro. 

Como é da praxe neste tipo de linguagens, as variáveis deverão ser declaradas no início do programa e não pode haver re-declaração, nem utilização sem declaração prévia. 
Se nada for explicitado, o valor da variável após a declaração é 0 (zero). 

Desenvolva, então, um compilador para essa linguagem com base na GIC criada acima e com recurso aos módulos Yacc/ Lex do PLY/Python.

O compilador deve gerar pseudo-código, Assembly da Máquina Virtual VM. 

Muito Importante: Para a entrega do TP deve preparar um conjunto de testes (programas-fonte escritos na sua linguagem) e mostrar o código Assembly gerado bem como o programa a correr na máquina virtual VM. 

Esse conjunto terá de conter, no mínimo, os 4 primeiros exemplos abaixo e um dos 2 últimos conforme a sua escolha acima: 

• ler 4 números e dizer se podem ser os lados de um quadrado. 

• ler um inteiro N, depois ler N números e escrever o menor deles. 

• ler N (constante do programa) números e calcular e imprimir o seu produtório.

• contar e imprimir os números impares de uma sequˆencia de números naturais. 

• ler e armazenar N números num array; imprimir os valores por ordem inversa. 

• invocar e usar num programa seu uma função ’potencia()’, que começa por ler do input a base B e o expoente E E e retorna o valor B .
