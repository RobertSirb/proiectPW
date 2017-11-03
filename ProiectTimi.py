# Read in a WAV and find the freq's
import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt
import struct
from scipy import signal
chunk = 4096
from FrequncyEstimator import freq_from_autocorr
def stereo_to_mono(hex1, hex2):
    """average two hex string samples"""
    return hex((ord(hex1) + ord(hex2))/2)
def pause():
    raw_input("Press the <ENTER> key to continue...")
# open up a wave
wf = wave.open('blueMic.wav', 'rb')
swidth = wf.getsampwidth()
RATE = wf.getframerate()
print RATE
# use a Blackman window
window = np.blackman(chunk)
# open stream
p = pyaudio.PyAudio()
stream = p.open(format =
                p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = RATE,
                output = True)



# read some data
data = wf.readframes(chunk)
new_frames=''
# play stream and find the frequency of each chunk
frec=[]
counter=0
while len(data) == chunk*swidth:
    # write data out to the audio stream
    counter+=1
    stream.write(data)
    # unpack the data and times by the hamming window
    
    #plt.plot(data)
    #plt.show()
    #print data
    indata = np.array(wave.struct.unpack("%dh"%(len(data)/swidth),\
                                         data))
    freq_in_hertz=freq_from_autocorr(indata, RATE) 
    print '%f Hz' % freq_in_hertz
    frec.append([freq_in_hertz,data])
    if freq_in_hertz >169 and freq_in_hertz <180:
        indata2=indata#*window
        w=abs(np.fft.fft(indata2))
        for it in range(169,180):
            w[it]=0
        y=np.fft.ifft(w)
        plt.plot(indata)
        plt.show()
        plt.plot(y)
        plt.show()
        freq_in_hertz=freq_from_autocorr(y, RATE) 
        print ' A doua frec %f Hz' % freq_in_hertz
        pause()
    '''
    #indata = np.array(data)
    #print indata
    indata=indata*window
    plt.plot(indata)
    if counter>30:
        plt.show()
    # Take the fft and square each value
    w=abs(np.fft.fft(indata))**2
    freqs = np.fft.fftfreq(len(w))
    
    idx = np.argmax(np.abs(w))
    freq = freqs[idx]
    
    #print idx
    freq_in_hertz = abs(freq * RATE)
    print(freq_in_hertz) ,"fft"
    #frec.append([freq_in_hertz,data])
    plt.plot(freqs*RATE,w)
    plt.xlim([0,2000])
    if counter>30:
        plt.show()
    
    # find the maximum
    which = fftData[1:].argmax() + 1
    # use quadratic interpolation around the max
    if which != len(fftData)-1:
        y0,y1,y2 = np.log(fftData[which-1:which+2:])
        #print fftData[which-1:which+2:]
        x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
        # find the frequency and output it
        thefreq = (which+x1)*RATE/chunk
        print "The freq is %f Hz." % (thefreq)
        freq.append(thefreq)
    else:
        thefreq = which*RATE/chunk
        print "The freq is %f Hz." % (thefreq)
        freq.append(thefreq)
    '''
    # read some more data
    data = wf.readframes(chunk)
    new_frames=''
# play stream and find the frequency of each chunk
if data:
    stream.write(data)
pause()
freq2=[]
for it in frec:
    if it[0] >70 and it[0]<450:
        freq2.append(it)
for it in freq2:
    print it[0]
    stream.write(it[1])
    pause()
stream.close()
p.terminate()
#print freq

couter=0
for it in freq2:
    if it <70 or it >5:
        #print it
        couter+=1
#print couter  