'''
Created on Oct 27, 2017

@author: Pita
'''
dataBase={}

def addToDataBase(songName,songHash):
    global dataBase
    dataBase[songName]=songHash
def getSongHas(song):
    global dataBase
    return dataBase[song]
def findClosestSongs(songHash,songName=''):
    global dataBase
    myList=[]
    for currSong,currHash in dataBase.iteritems():
        myList.append([abs(hash-currHash),currSong])
    myList.sort(key= lambda x : x[0])
    songList=[]
    for it in myList:
        songList.append(it[1])
    return songList