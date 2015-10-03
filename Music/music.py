import numpy as np
import random

root = 0
good = 1
ok = 2
bad = 3
size_rhythm = 4



def getNote(array):
    x = random.random()
    for i in range(len(array)):

        if x < array[i]:
            break
    return i+1

def makeArray(Notes):
    pgood = 0.75
    pok = 0.2
    pbad = 0.05
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

def pickBassBeat(Array):
    picks = [0] * size_rhythm
    for i in range(size_rhythm):
        x = random.randint(0,len(Array))
        picks[i]= x

    return picks

M7 = [0,3,2,3,1,2,3,1,3,2,3,1,1]
m7 = [0,3,2,1,3,2,3,1,2,3,1,3,1]
Mpent = [0,3,2,3,1,1,3,1,3,2,3,2,1]
mpent = [0,3,2,1,3,1,3,1,2,3,2,3,1]
m7 = makeArray(m7)
M7 = makeArray(M7)
Mpent = makeArray(Mpent)
mpent = makeArray(mpent)


rhyArr = []
rhyArr.append([8,8,8,8])
rhyArr.append([4,4])
rhyArr.append([8,8,4])
rhyArr.append([8,4,8])
rhyArr.append([16,16,4,16,16])

pickBassBeat(rhyArr)
num_notes=0
music = []
for i in range(size_rhythm):
    for j in rhyArr[i]:
        note = 0
        if j != 0:
            note = getNote(m7)
        music.append([note,j])

notes = ['r', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b', 'c5']
for note in music:
    note[0] = notes[note[0]]

import pysynth
pysynth.make_wav(music, fn='out.wav')
