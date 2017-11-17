'''
Created on Nov 3, 2017

@author: Pita
'''
from __future__ import absolute_import
import numpy
from  PIL import Image
import imagehash

lungimeBucataMelodie=64 # ~ 6 sec de cantec
radicalLBM=8
numarIntervaluri=5

def obtineImagineDinFrecvente(frecvente):
    vectorImagini=[]
    vectorCurent=numpy.array([])
    it=0
    jt=0
    while it <len(frecvente)-lungimeBucataMelodie:
        vectorCurent=numpy.array([])
        jt=0
        while jt<lungimeBucataMelodie:
            vectorCurent=numpy.concatenate((vectorCurent,frecvente[it]))
            it+=1
            jt+=1
        vectorCurent = vectorCurent.reshape((radicalLBM , numarIntervaluri*radicalLBM))
        vectorImagini.append(vectorCurent)
    return vectorImagini
def obtineHashDinImagini(imaginiCantec):
    listaHashuri=[]
    k=0
    for it in imaginiCantec:
        temporar=Image.fromarray(it)
        hashLocal=imagehash.phash(temporar)
        listaHashuri.append(str(hashLocal))
        temporar=temporar.convert("RGB")
        temporar.save(r"imagine"+str(k)+".jpeg")
        k+=1
    listaHashuri=[int(hex_str, 16) for hex_str in listaHashuri]
    return listaHashuri
def obtineHash(frecvente):
    imaginiCantec=obtineImagineDinFrecvente(frecvente)
    listaHashuri = obtineHashDinImagini(imaginiCantec)
    print listaHashuri
    return listaHashuri