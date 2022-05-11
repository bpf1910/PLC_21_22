import re

f = open("inscritos.txt", "r", encoding="utf8")
#Cria/Reescreve ficheiro .JSON para escrita
g = open("E.JSON", "w", encoding="utf8")

#Ignora a primeira linha
next(f)
cabecalho = f.readline()
text = f.readlines()[0:20]

#Cada parâmetro do cabeçalho está separado por \t
cab = re.split(r'\t', cabecalho)

g.write("[\n")

#A variável 'j' vai percorrer os registos que nos interessam
for j in range(len(text)-1): 
    
    g.write("\t{\n")
    y = re.split(r'\t', text[j])
    
    #A variável 'i' vai percorrer cada posição do cabeçalho
    for i in range(len(y)-1):
        g.write("\t\t" + "\"" + cab[i] + "\"" + ":" + ' ' + "\"" + y[i] + "\"" + "," + "\n")

    g.write("\t\t" + "\"" + cab[i+1][:-1] + "\"" + ":" + ' ' + "\"" + y[i+1][:-1] + "\"" + "\n")
    g.write("\t},\n")

#O último elemento
g.write("\t{\n")
w = re.split(r'\t', text[j + 1])

for i in range(len(w)-1):
    g.write("\t\t" + "\"" + cab[i] + "\"" + ":" + ' ' + "\"" + w[i] + "\"" + "," + "\n")
    
g.write("\t\t" + "\"" + cab[i+1][:-1] + "\"" + ":" + ' ' + "\"" + y[i+1][:-1] + "\"" + "\n")
g.write("\t}\n")

g.write("]")

f.close()
g.close()