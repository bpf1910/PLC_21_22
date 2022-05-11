import re

f = open("inscritos.txt", "r", encoding="utf8")

#Lista que vai guardar as provas e os números de tarifário Vodafone de concorrentes cujo nome seja Paulo ou Ricardo
part = []
#As duas primeiras linhas não nos são importantes
text = f.readlines()[2:]

for line in text:
    
    #As colunas do ficheiro a ler estão separadas por \t
    y = re.split(r'\t', line)
    
    #Expressões regulares que vão filtrar os dados pretendidos
    nome = re.search(r'(?i:paulo)|(?i:ricardo)', y[19])
    insc = re.search(r'(?i:confirmada)|(?i:registada)', y[2])
    num = re.search(r'91[0-9]{7}', y[10])

    #O concorrente tem de ter a inscrição confirmada, tarifário Vodafone e Paulo ou Ricardo como nome
    if(nome and insc and num):
        aux = []
        #Nome (Coluna 20)
        aux.append(y[19])
        #Tipo de Inscrição (Coluna 5)
        aux.append(y[4])
        #Telefone/ Telemóvel (Coluna 11)
        aux.append(y[10])
        part.append(aux)

#Concorrentes organizados por prova e por nome
part.sort(key = lambda x : (x[1],x[0]))

#Limites da tabela
n_max, p_max, v_max = 4, 5, 6
for l in part:
    if len(l[0]) > n_max:
        n_max = len(l[0])
    if len(l[1]) > p_max:
        p_max = len(l[1])
    if len(l[2]) > v_max:
        v_max = len(l[2])

#Desenhar a tabela
print("Provas dos concorrentes cujo nome contém Paulo ou Ricardo\n")
print("| Nome"+' '*(n_max-4)+" | Prova"+' '*(p_max-5)+" | Número"+' '*(v_max-6)+' |')
print("|-"+'-'*(n_max)+"-|-"+'-'*(p_max)+"-|-"+'-'*(v_max)+'-|')
for ins in part:
    print('| '+ins[0]+' '*(n_max-len(ins[0]))+" | "+ins[1]+' '*(p_max-len(ins[1]))+" | "+ins[2]+' '*(v_max-len(ins[2]))+' |')

f.close()