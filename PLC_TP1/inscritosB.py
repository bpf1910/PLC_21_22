import re


f = open('inscritos.txt', "r", encoding="utf8")

#Lista que vai guardar concorrentes individuais de Valongo
part = []
#As duas primeiras linhas não nos são importantes
text = f.readlines()[2:]

for line in text:
    
    #As colunas do ficheiro a ler estão separadas por \t
    y = re.split(r'\t', line)
    
    #Expressões regulares que vão filtrar os dados pretendidos
    tipo = re.search(r'(?i:individual)', y[9])
    morada = re.search(r'(?i:valongo)', y[20])
    insc = re.search(r'(?i:confirmada)|(?i:registada)', y[2])

    #O concorrente tem de ser individual, ser de Valongo e não ter a inscrição expirada
    if(tipo and morada and insc):
        aux = []
        #Nome (Coluna 20)
        aux.append(y[19])
        #Morada (Coluna 21)
        aux.append(y[20])
        part.append(aux)

#Concorrentes organizados por nome
part.sort(key = lambda x : x[0])

#Limites da tabela
n_max, m_max = 4, 6
for l in part:
    if len(l[0]) > n_max:
        n_max = len(l[0])
    if len(l[1]) > m_max:
        m_max = len(l[1])

#Desenhar a tabela
print("Concorrentes de Valongo que se inscrevem como \"Individual\"\n")
print("| Nome"+' '*(n_max-4)+" | Morada"+' '*(m_max-6)+' |')
print("|-"+'-'*(n_max)+"-|-"+'-'*(m_max)+'-|')
for ins in part:
    print('| '+ins[0]+' '*(n_max-len(ins[0]))+" | "+ins[1]+' '*(m_max-len(ins[1]))+' |')

f.close()