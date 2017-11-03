'''
Created on Nov 3, 2017

@author: Pita
'''
import subprocess
numarCanale="1"
formatMonstra="s16"
rataEsantionare="44100"
codificare="pcm_s16le"
formatFisier="wav"

def obtineArgumente(melodie):
    argumente=["ffmpeg"]
    """
    argumente.append("-i")
    argumente.append(melodie)
    argumente.append("-ac")
    argumente.append(numarCanale)
    argumente.append("-ar")
    argumente.append(rataEsantionare)
    argumente.append("-acodec")
    argumente.append(codificare)
    argumente.append("-sample_fmt")
    argumente.append(formatMonstra)
    numeFisierIesire=melodie.split(".")[0]
    numeFisierIesire+="."+formatFisier+'"'
    argumente.append(numeFisierIesire)
    return argumente , numeFisierIesire
    """
    return argumente,""
def convertesteMelodie(melodie):
    argumente,numeFisierIesire=obtineArgumente(melodie)
    valoareReturnata=subprocess.call(argumente)
    if 0 != valoareReturnata:
        return -1 , "Nu pot converti melodia la formatul necesar!"
    return 0,numeFisierIesire

convertesteMelodie('"C:\\Users\\Pita\\Desktop\\New folder\\REC_20171029_212348.m4a"')