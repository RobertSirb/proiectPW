'''
Created on Oct 26, 2017

@author: Pita
'''
from PIL import Image
import math
import struct
import imagehash
import dummyDataBase
import random
import numpy
from sympy.ntheory.generate import prime
def main(songName, songData):
    global f2
    d1=int(math.sqrt(len(songData)))
    songData=songData[:d1*d1]
    songData=numpy.array(songData).reshape((d1,d1))
    #imageData=struct.pack("%dl"%len(songData),*songData)
    #print imageData
    temporar=Image.fromarray(songData)
    temporar=temporar.convert("RGB")
    temporar.save(songName)
    for it in temporar.getcolors(60000):
        f2.write(str(it[1])+" ")
    songHash=imagehash.phash(temporar)
    #print songHash
    #temporar.show()
    return songHash

testSongData=[]
for it in range(2000):
    testSongData.append(random.uniform(30.00, 40.00)) 
    testSongData.append(random.uniform(40.00, 80.00))
    testSongData.append(random.uniform(80.00, 120.00))
    testSongData.append(random.uniform(120.00, 180.00))
    testSongData.append(random.uniform(180.00, 4200.00))
f1=open("vectorIntrare.txt","w")
f2=open("vectorIesire.txt","w")
for it in testSongData:
    f1.write(str(it)+" ")
print testSongData
songHash=[]
#for it in range(len(testSongData)/605):
    #songHash.append(main("bucata",testSongData[605*it:605*it+605]))
print main("temporar.jpeg",testSongData)
#testSongData[2374]=0.0
for it in range(len(testSongData)):
    testSongData[it]=testSongData[it] * ((2.0**(1.0/12.0))**6.0)
print main("temporar2.jpeg",testSongData)
print prime(350)
f1.close()
f2.close()
