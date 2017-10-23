# Read in a WAV and find the freq's
import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt
import struct
chunk = 1024
def stereo_to_mono(hex1, hex2):
    """average two hex string samples"""
    return hex((ord(hex1) + ord(hex2))/2)
def pause():
    programPause = raw_input("Press the <ENTER> key to continue...")
# open up a wave
wf = wave.open('file.wav', 'rb')
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
    #indata = np.array(data)
    #print indata
    indata=indata*window
    plt.plot(indata)
    #if counter>30:
    #plt.show()
    # Take the fft and square each value
    w=abs(np.fft.fft(indata))
    freqs = np.fft.fftfreq(len(w))
    
    idx = np.argmax(np.abs(w))
    freq = freqs[idx]
    plt.plot(freqs*RATE,w)
    #print idx
    freq_in_hertz = abs(freq * RATE)
    print(freq_in_hertz)
    frec.append([freq_in_hertz,data])
    #if counter>30:
    #plt.show()
    # find the maximum
    '''
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
    if it[0] >70 and it[0]<500:
        freq2.append(it)
for it in freq2:
    print it[0]
    stream.write(it[1])
stream.close()
p.terminate()
#print freq

couter=0
for it in freq2:
    if it <70 or it >5:
        #print it
        couter+=1
#print couter 