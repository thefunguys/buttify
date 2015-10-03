import numpy as np
import random

root = 0
good = 1
ok = 2
bad = 3
size_rhythm = 4
bass_bottom = 8



def getNote(array):
    x = random.random()
    for i in range(len(array)):

        if x < array[i]:
            break
    return i+1

def makeArray(Notes):
    pgood = 0.85
    pok = 0.12
    pbad = 0.03
    ngood = 0.
    nok = 0.
    nbad = 0.
    for i in Notes:
        if(i == root):
            ngood = ngood + 2.
        elif(i == good):
            ngood = ngood + 1.
        elif(i == ok):
            nok = nok + 1.
        else:
            nbad = nbad + 1.

    prob = 0.0
    for i in range(len(Notes)):
        if(Notes[i] == root):
            Notes[i] = 2*pgood/ngood + prob
        elif(Notes[i] == good):
            Notes[i] = pgood/ngood + prob
        elif(Notes[i] == ok):
            Notes[i] = pok/nok + prob
        else:
            Notes[i] = pbad/nbad + prob

        prob = Notes[i]

    return Notes


def readNotes():
    f = open("notes.txt","r")
    array = []
    for line in f:
        array.append(line.split(" "))


    notes = []
    for line in array:
        notes.append(line[1])

    return notes



def pickBassBeat(Array):
    picks = [0] * size_rhythm
    for i in range(size_rhythm):
        x = random.randint(0,len(Array))
        picks[i]= x

    return picks

def BassLine(beat,prog,notes,scales):
    music = []
    for k in prog:
        for rhy_pat in beat:
            for j in rhy_pat:
                val = 0
                if j != 0:
                    if k == 10:
                        val = getNote(scales[3])
                    else:
                        val = getNote(scales[2])
                    letter = notes[val + bass_bottom + k - 1]
                else:
                    letter = 'r'
                    j=16
                    
                music.append([letter,j])
        
    return music


notes = readNotes()

I_V = [1,8,10,6]
vi_IV = [10,6,1,8]
IV_I = [6,1,8,10]


scales = []
M7 = [0,3,2,3,1,2,3,1,3,2,3,1,1]
m7 = [0,3,2,1,3,2,3,1,2,3,1,3,1]
Mpent = [0,3,2,3,1,1,3,1,3,2,3,2,1]
mpent = [0,3,2,1,3,1,3,1,2,3,2,3,1]
scales.append(makeArray(M7))
scales.append(makeArray(m7))
scales.append(makeArray(Mpent))
scales.append(makeArray(mpent))


rhyArr = []
rhyArr.append([2,2,2,2])
rhyArr.append([4,4])
rhyArr.append([2,2,4])
rhyArr.append([2,4,2])
rhyArr.append([0,0,4,0,0])

beat = []
picks = pickBassBeat(rhyArr)
for i in range(size_rhythm):
    beat.append(rhyArr[i])

num_notes=0


#for i in range(size_rhythm):
music = BassLine(beat,I_V,notes, scales)
print music


import pysynth as pysynth
pysynth.make_wav(music, fn="bass.wav")



