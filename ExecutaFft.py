'''
Created on Oct 20, 2017

@author: Pita
'''
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile # get the api
fs, data = wavfile.read('bass.wav') # load the data
#print data
a = data.T[0] # this is a two channel soundtrack, I get the first track
print a
print len(a)
b=[(ele/2**16.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
c = fft(b) # calculate fourier transform (complex numbers list)
d = len(c)/2  # you only need half of the fft list (real signal symmetry)
plt.plot(abs(c[:(d-1)]),'r') 
plt.show()