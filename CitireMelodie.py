'''
Created on Oct 20, 2017

@author: Pita
'''
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack  import fft ,rfft
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

chunk = 2048
window = np.blackman(chunk)
oct2=wave.open("bass.wav")
print oct2.getparams()
data2=oct2.getnframes()
data2=oct2.readframes(data2)
freq,data2=wav.read("bass.wav")
data2=data2[:, 1]
print data2,len(data2)
k=0
t=160
while k<t:
    data=data2[k*chunk:(k+1)*chunk]
    #plt.plot(data)
    #plt.show()
    data=data*window
    #plt.plot(data)
    #plt.show()
    fftData=abs(np.fft.rfft(data))**2
    #plt.plot(fftData)
    #plt.show()
    which = fftData[1:].argmax() + 1
    # use quadratic interpolation around the max
    if which != len(fftData)-1:
        y0,y1,y2 = np.log(fftData[which-1:which+2:])
        #print fftData[which-1:which+2:]
        x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
        # find the frequency and output it
        thefreq = (which+x1)*freq/chunk
        print "The freq is %f Hz." % (thefreq)
    else:
        thefreq = which*freq/chunk
        print "The freq is %f Hz." % (thefreq)
    k=k+1
    # read some more data