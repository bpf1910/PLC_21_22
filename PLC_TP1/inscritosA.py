import re

f = open("inscritos.txt", "r", encoding="utf8")

#Lista que vai guardar os concorrentes entre as posições 5 e 15
part = []
#As duas primeiras linhas não nos são importantes
text = f.readlines()[2:]

for line in text:
    
    #As colunas do ficheiro a ler estão separadas por \t
    y = re.split(r'\t', line)

    #O concorrente tem de estar numa posição entre 5 e 15
    x = re.fullmatch(r'[5-9]|1[0-5]', y[7])
    if x:
        aux=[]
        #Nome (Coluna 20)
        aux.append(y[19])
        #Email (Coluna 28) (-1 remove o \n)
        aux.append(y[27][:-1])
        #Num. Participante no Evento (Coluna 8)
        aux.append(int(y[7]))
        part.append(aux)

#Concorrentes organizados por posição        
part.sort(key = lambda x : x[2])

#Limites da tabela
p_max, n_max, e_max = 7, 4, 5
for l in part:
    if len(str(l[2])) > p_max:
        p_max = len(str(l[2]))
    if len(l[0]) > n_max:
        n_max = len(l[0])
    if len(l[1]) > e_max:
        e_max = len(l[1])

#Desenhar a tabela
print("Nome e Email dos concorrentes inscritos entre a 5ª e a 15ª posição\n")
print("| Posição"+' '*(p_max-7)+" | Nome"+' '*(n_max-4)+" | Email"+' '*(e_max-5)+' |')
print("|-"+'-'*(p_max)+"-|-"+'-'*(n_max)+"-|-"+'-'*(e_max)+'-|')
for ins in part:
    print('| '+str(ins[2])+' '*(p_max-len(str(ins[2])))+" | "+ins[0]+' '*(n_max-len(ins[0]))+" | "+ins[1]+' '*(e_max-len(ins[1]))+' |')

f.close()