'''
Created on Oct 20, 2017

@author: Pita
'''
import math
RANGE = [40, 80, 120, 180, 300 ]

def getIndex(freq):
    i = 0;
    while (RANGE[i] < freq):
        i+=1
    return i
FUZ_FACTOR=1
def hashMeu(p1, p2, p3, p4) :
    return (p4 - (p4 % FUZ_FACTOR)) * 100000000 + (p3 - (p3 % FUZ_FACTOR))* 100000 + (p2 - (p2 % FUZ_FACTOR)) * 100 + (p1 - (p1 % FUZ_FACTOR))
def absMeu(lst):
    return abs(lst[1])
def main(result):
    highscores=[]
    points=[]
    for t in range(len(result)):
        highscores.append([])
        points.append([])
        for index in range(6):
            highscores[t].append(float("-inf"))
            points[t].append(0)
    hashuri=[]
    for t in range(len(result)):
        for freq in range(40,300):
            mag = math.log(abs(result[t][freq]) + 1);
    
            index = getIndex(freq);
    
            if mag > highscores[t][index] :
                highscores[t][index] = mag
                points[t][index] = freq
        h = hashMeu(points[t][0], points[t][1], points[t][2], points[t][3])
        hashuri.append(h)
    print hashuri
    f1=open("hash3.txt","w")
    for it in hashuri:
        f1.write(str(it)+" ")
    #f1.write(hashuri)
    f1.close()

