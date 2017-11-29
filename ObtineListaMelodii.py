'''
Created on Nov 3, 2017

@author: Pita
'''
from InterfataBazeDate import obtineToateMelodiile
maiSuntMelodiiInBazaDate = False

def hammingDistance(hash1,hash2):
    return bin(hash1^hash2).count('1')
def obtineLSV(hashLista1,hashLista2):
    rezervat={}
    for it in range(len(hashLista1)):
        distantaCurentaMinimaLibera=[1000,-1]
        distantaCurentaMinimaRezervata=[1000,-1]
        for jt in range(len(hashLista2)):
            if jt in rezervat:
                distanta=hammingDistance(hashLista1[it], hashLista2[jt])
                if distanta < distantaCurentaMinimaRezervata[0]:
                    distantaCurentaMinimaRezervata=[distanta,jt]
            else:
                distanta=hammingDistance(hashLista1[it], hashLista2[jt])
                if distanta < distantaCurentaMinimaLibera[0]:
                    distantaCurentaMinimaLibera=[distanta,jt]
        if distantaCurentaMinimaLibera[0] <= distantaCurentaMinimaRezervata[0]:
            rezervat[distantaCurentaMinimaLibera[1]]=it
        else:
            pozitieAtribuita=distantaCurentaMinimaRezervata[1]
            pozitieRezervata=rezervat[pozitieAtribuita]
            if hammingDistance(hashLista1[pozitieRezervata], hashLista2[pozitieAtribuita]) < hammingDistance(hashLista1[it], hashLista2[pozitieAtribuita]):
                rezervat[pozitieAtribuita]=pozitieRezervata
                rezervat[distantaCurentaMinimaLibera[1]]=it
            else:
                rezervat[pozitieAtribuita]=it
                rezervat[distantaCurentaMinimaLibera[1]]=pozitieRezervata
    distantaTotala=0
    for  key,val  in rezervat.items():
        distantaTotala+=hammingDistance(hashLista1[key], hashLista2[val])
    return distantaTotala
                    
                
            
            
def comparaDouaMelodi(hashMelodie1,hashMelodie2):
    return obtineLSV(hashMelodie1, hashMelodie2)
def obtineListaMelodii(hashLista1):
    listaTotalaMelodii=[]
    while (maiSuntMelodiiInBazaDate):
        maiSuntMelodiiInBazaDate,nume,hashListaMelodieBazaDate = obtineToateMelodiile()
        if maiSuntMelodiiInBazaDate:
            factorSimilaritate=comparaDouaMelodi(hashLista1,hashListaMelodieBazaDate)
            listaTotalaMelodii.append((nume,factorSimilaritate))
        else:
            break
    