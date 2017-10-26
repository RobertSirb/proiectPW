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
def main(songName, songData):
    d1=int(math.sqrt(len(songData)))
    songData=songData[:d1*d1]
    songData=numpy.array(songData).reshape((d1,d1))
    #imageData=struct.pack("%dl"%len(songData),*songData)
    #print imageData
    temporar=Image.fromarray(songData)
    #temporar=temporar.convert("RGB")
    #temporar.save("temporar.png")
    songHash=imagehash.phash(temporar)
    print songHash
    temporar.show()
    return dummyDataBase.findClosestSongs(songHash)

testSongData=[]
for it in range(2000):
    testSongData.append(random.uniform(30.00, 40.00)) 
    testSongData.append(random.uniform(40.00, 80.00))
    testSongData.append(random.uniform(80.00, 120.00))
    testSongData.append(random.uniform(120.00, 180.00))
    testSongData.append(random.uniform(180.00, 4200.00))
print testSongData
main("cantec",testSongData)

    
