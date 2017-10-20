'''
Created on Oct 20, 2017

@author: Pita
'''
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack  import fft
import numpy as np
import wave
import struct
import math
import GenerareHash
class Complex:
    def __init__(self,re,im):
        self.re=re
        self.im=im
    def plus(self,b):
        real=self.re+b.re
        imag=self.im+b.im
        return Complex(real,imag)
    def times(self,b):
        real=self.re*b.re-self.im*b.im
        imag=self.re*b.im+self.im*b.re
        return Complex(real,imag)
    def minus(self,b):
        real=self.re-b.re
        imag=self.im-b.im
        return Complex(real,imag)
    def toList(self):
        return [self.re,self.im]
def pause():
    programPause = raw_input("Press the <ENTER> key to continue...")
        
def fft2(x):
    N = len(x)
    if N==0:
        return [[]]
    #print N
    #pause()
    even = []
    for k in range(N/2):
        even.append(x[2 * k])
    
    q = fft(even)

    odd = [] 
    for k in range(N/2):
        odd.append(x[2 * k + 1])
    
    r = fft(odd)

    y=[]
    for k in range(N):
        y.append(Complex(0,0))
    
    for k in range(N/2):
        kth = -2.0 * float(k) * math.pi / float(N)
        wk = Complex(math.cos(kth), math.sin(kth))
        y[k] = q[k].plus(wk.times(r[k]))
        y[k + N / 2] = q[k].minus(wk.times(r[k]))
        
    return y



oct2=wave.open("bass.wav")
print oct2.getparams()
data2=oct2.getnframes()
data2=oct2.readframes(data2)
print len(data2)
audio  = []
for it in data2:
    audio.append(it)
totalSize = len(audio)
chunkSize=4*1024
nrChunks = totalSize/chunkSize;
#nrChunks = 20
print nrChunks
result = [];

for j in range(nrChunks):
    complexArray=[]
    for i in range(chunkSize):
        nr=struct.unpack("b",audio[(j*chunkSize)+i])
        nr=int(nr[0])
        complexArray.append([nr, 0])
    result.append(fft(complexArray))

#print result[0][299]
#plt.plot(result[0])
#plt.show()
oct2.close()
GenerareHash.main(result)
