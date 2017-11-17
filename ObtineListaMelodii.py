'''
Created on Nov 3, 2017

@author: Pita
'''
maiSuntMelodiiInBazaDate = False
def hammingDistance(hash1,hash2):
    return bin(hash1^hash2).count('1')
def comparaDouaMelodi(hashMelodie1,hashMelodie2):
    pass
def obtineHashListaMelodieBazaDate():
    pass
def obtineListaMelodii(hashLista):
    while (maiSuntMelodiiInBazaDate):
        nume,hashListaMelodieBazaDate = obtineHashListaMelodieBazaDate()
    factorSimilaritate=comparaDouaMelodi(hashLista,hashListaMelodieBazaDate)
    