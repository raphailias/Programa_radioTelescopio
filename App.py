import matplotlib.pyplot as plt 
file = open('3C273.txt', 'r')
lista = file.readlines()
lista2 =[]
listaPar=[]
listaImpar=[]
paridade=1
for line in lista:
    line =line.rstrip()
    try:
        lista2.append(float(line))
    except:
        if(len(lista2)>0):
            if(paridade==1):
                listaPar.append(lista2)
            else:
                listaImpar.append(lista2)
            lista2=[]
            paridade*=-1
eixox=[]
for i in range(len(listaPar[0])):
    eixox.append(-10.59+0.26*i)
mediasImpar=[]
mediasPar=[] 
for i in range(len(listaPar[0])):
    mediaImpar=0
    mediaPar=0 
    for j in range(len(listaPar)):
        mediaImpar+=listaImpar[j][i]
        mediaPar+=listaPar[j][i]
    mediaPar=mediaPar/len(listaPar[0])
    mediaImpar=mediaImpar/len(listaImpar[0])
    mediasImpar.append(mediaImpar)
    mediasPar.append(mediaPar)
plt.plot(eixox,mediasPar) 
plt.plot(eixox,mediasImpar)
plt.show()
