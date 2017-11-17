'''
Created on Nov 3, 2017

@author: Pita
'''
import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt
import struct
import math
from scipy import signal
from ObtineHash import obtineHash
RANGE = [40 , 80 , 120 , 180 , 300]
def getIndex(freq): 
    i = 0
    while RANGE[i] < freq:
        i+=1
    return i

def deschideMelodie(melodie):
    wf=wave.open(melodie, 'rb')
    return wf
def obtineFrecventeDominante(vectorFFT):
    frecventeDominante=[0]*5
    frecventeDominante=np.array(frecventeDominante)
    for freq in range(40,300):
        mag=abs(vectorFFT[freq])+1
        index=getIndex(freq)
        if(mag>frecventeDominante[index]):
            frecventeDominante[index]=freq
    return frecventeDominante
def executaFFT(melodie):
    chunk = 4096
    wf = deschideMelodie(melodie)
    swidth = wf.getsampwidth()
    RATE = wf.getframerate()
    data = wf.readframes(chunk)
    frecventeMelodie=[]
    while len(data) == chunk*swidth:
        indata = np.array(wave.struct.unpack("%dh"%(len(data)/swidth),data))
        
        frecventeMelodie.append(obtineFrecventeDominante(np.fft.fft(indata)))
        data = wf.readframes(chunk)
    #test part
    obtineHash(frecventeMelodie)
    #end test part
    return frecventeMelodie

executaFFT(r'C:\Users\Pita\Desktop\New folder\REC_20171029_212348.wav')