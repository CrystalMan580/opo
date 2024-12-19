from numpy import array
from math import sqrt


global xd , yd

xd = float(input("Donner xd: "))
yd = float(input("Donner yd: "))


def saisie():
    n = int(input("donner le nombre de cases n"))
    while not (n%2==0 and 4<=n<=50):
        n=int(input("donner le nobre de cases n"))
    return(n)

def remplire(bat,n):
    for i in range(n):
        bat[i]=dict()
        bat[i]["nom"]=input("donner votre nom")
        while not (len(bat[i]["nom"])<=15 ):
            bat[i]["nom"]=input("donner votre nom")
        bat[i]["xb"]=float(input("donner xb"))
        bat[i]["yb"]=float(input("donner yb"))
        while not(verif(bat[i]["xb"],bat[i]["yb"]) == True):
            bat[i]["xb"]=float(input("donner xb"))
            bat[i]["yb"]=float(input("donner yb"))
def verif(bat):
    s=0
    test=True
    while(s<n and test==True):
        if (Tab[i]["xb"]==x and Tab[i]["yb"]==y):
            test=False
        else:
            s+=1
    return(test)
def generer_distance(dist,bat,n):
    for i in range(n):
        dist[i]=sqrt((xd-bat[i]["xb"])*(xd-bat[i]["xb"])+(yd-bat[i]["yb"])*(yd-bat[i]["yb"]))
def tri(dist,bat,n):
    echange=True
    while(echange==True and n!=1):
        echange=False
        for i in range(n):
            if(dist[i]>dist[i+1]):
                aux=dist[i]
                dist[i]=dist[i+1]
                dist[i+1]=aux
                test=bat[i]["nom"]
                bat[i]["nom"]=bat[i+1]["nom"]
                bat[i+1]["nom"]=test
                auy=bat[i]["xb"]
                bat[i]["xb"]=bat[i][i+1]
                bat[i]["xb"]=auy
                aut=bat[i]["yb"]
                bat[i]["yb"]=bat[i+1]["yb"]
                bat[i+1]["yb"]=aut
        n=n-1
def afficher(dist,bat,n):
    for i in range(n):
        print(bat[i]["nom"],dist[i])

#pp 
n=saisie()
bat=array([dict()]*n)
remplire(bat,n)
dist=array([float()]*n)
generer_distance(dist,bat,n,xd,yd)
tri(dist,bat,n,xd,yd)
aff(dist,bat,n)
                

        

