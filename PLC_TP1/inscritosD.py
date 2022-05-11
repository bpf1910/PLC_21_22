import re

f = open('inscritos.txt',encoding="utf8")

#salta as duas primeira linhas (título e cabeçalho)
next(f)
next(f)

#lista com os nomes dos responsáveis sem repetições
nomes = []

#para os limites da tabela
n_max = 19

for line in f:
    #se a lista possuir 20 elementos o ciclo pára
    if len(nomes)==20:
        break

    #só precisamos de ir buscar o primeiro campo (nome do responsável)
    campos = re.split('\t', line, maxsplit=1)
    
    #se o nome do responsável que está a ser tratado ainda não estiver na lista é adicionado
    if campos[0].lower() not in nomes:
        nomes.append(campos[0].lower())

        #limites da tabela
        if len(campos[0])>n_max:
            n_max = len(campos[0])

#desenhar a tabela
print("Os 20 primeiros Responsáveis de Equipa (nome em minúsculas s/ repetições)\n")
print("| Nome do Responsável"+' '*(n_max-19)+' |')
print("|-"+ "-"*(n_max)+'-|')
for n in nomes:
    print('| '+n+' '*(n_max-len(n))+' |')

f.close()


