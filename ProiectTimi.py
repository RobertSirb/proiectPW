# Read in a WAV and find the freq's
import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt
chunk = 22050
def stereo_to_mono(hex1, hex2):
    """average two hex string samples"""
    return hex((ord(hex1) + ord(hex2))/2)
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
freq=[]
counter=0
while len(data) == chunk*swidth:
    # write data out to the audio stream
    counter+=1
    stream.write(data)
    # unpack the data and times by the hamming window
    
    #plt.plot(data)
    #plt.show()
    #print data
    indata = np.array(wave.struct.unpack("%dh"%(len(data)/swidth),data))
    #print indata
    indata=indata*window
    plt.plot(indata)
    #if counter>30:
    plt.show()
    # Take the fft and square each value
    w=abs(np.fft.rfft(indata))
    freqs = np.fft.fftfreq(len(w))
    plt.plot(w)
    idx = np.argmax(np.abs(w))
    freq = freqs[idx]
    freq_in_hertz = abs(freq * 44100)
    print(freq_in_hertz)
    #if counter>30:
    plt.show()
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
stream.close()
p.terminate()
#print freq
freq2=[]
for it in freq:
    if it >220.00 and it<1000:
        freq2.append(it)
print freq2
print len(freq2)
couter=0
for it in freq2:
    if it <508.565 or it >538.81:
        print it
        couter+=1
print couter 