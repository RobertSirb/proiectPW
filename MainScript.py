'''
Created on Nov 3, 2017

@author: Pita
'''
from ConvertesteMelodie import convertesteMelodie
from ExecutaFFT import executaFFT
from ObtineHash import obtineHash
from ObtineListaMelodii import obtineListaMelodii

import sys
def exitWithError(mesaj):
    sys.exit(mesaj) 
def verificaValoareReturnata(cod , mesaj):
    if 0 != cod:
        exitWithError(mesaj)
if __name__ == '__main__':
    
    if len(sys.argv) != 2 :
        exitWithError("Argumente invalide !")
        
    valoareReturnata,melodie=convertesteMelodie(sys.argv[1])
    verificaValoareReturnata(valoareReturnata,melodie)
    
    valoareReturnata , frecvente = executaFFT(melodie)
    verificaValoareReturnata(valoareReturnata, frecvente)
    
    valoareReturnata , hashuri = obtineHash(frecvente)
    verificaValoareReturnata(valoareReturnata, hashuri)
    
    valoareReturnata , melodii = obtineListaMelodii(hashuri)
    verificaValoareReturnata(valoareReturnata, melodii)
    
    return melodii