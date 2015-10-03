import numpy as np
import random

root = 0
good = 1
ok = 2
bad = 3
bass_bottom = 8
M7 = [0,3,2,3,1,2,3,1,3,2,3,1,1]
m7 = [0,3,2,1,3,2,3,1,2,3,1,3,1]
Mpent = [0,3,2,3,1,1,3,1,3,2,3,2,1]
mpent = [0,3,2,1,3,1,3,1,2,3,2,3,1]



def getNote(array):
    x = random.random()
    for i in range(len(array)):

        if x < array[i]:
            break
    return i+1

def makeArray(Notes, pgood, pok, pbad):
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



def pickBeat(Array, size_rhythm):
    picks = [0] * size_rhythm
    for i in range(size_rhythm):
        x = random.randint(0,len(Array))
        picks[i]= x

    return picks

def GetLine(beat,prog,notes,M, m, bottom):
    music = []
    
    for k in prog:
        for rhy_pat in beat:
            for j in rhy_pat:
                val = 0
                if j != 0:
                    if k == 10:
                        val = getNote(m)
                    else:
                        val = getNote(M)
                    letter = notes[val + bottom + k - 1]
                else:
                    letter = 'r'
                    j=16
                    
                music.append([letter,j])
        
    return music




notes = readNotes()

I_V = [1,8,10,6]
vi_IV = [10,6,1,8]
IV_I = [6,1,8,10]



guitar_rhy = []
guitar_rhy.append([8,8,8,8,8,8,8,8])
guitar_rhy.append([8,16,16,16,16,16,16,16,16,8,4])
guitar_rhy.append([8,16,8,16,-8,16,8,8,16,16])
guitar_rhy.append([-8,16,16,16,16,8,8,16,16,16,8])
guitar_rhy.append([-8,-8,4,8,4])
guitar_rhy.append([-8,-8,-8,-8,16,-8])


bass_rhy = []
bass_rhy.append([8,8,8,8])
bass_rhy.append([8,8,8,8])
bass_rhy.append([8,8,8,8])
bass_rhy.append([8,8,8,8])
bass_rhy.append([8,8,8,8])
bass_rhy.append([8,8,8,8])


Bass_beat = []
bass_size = 4
Guitar_beat = []
guitar_size = 2

picks = pickBeat(bass_rhy,bass_size)
for i in range(bass_size):
    Bass_beat.append(bass_rhy[i])

picks = pickBeat(guitar_rhy,guitar_size)
for i in range(guitar_size):
    Guitar_beat.append(guitar_rhy[i])

M7 = makeArray(M7, 0.75, 0.2, 0.05)
m7 = makeArray(m7, 0.75, 0.2, 0.05)
Mpent = makeArray(Mpent, 0.9, 0.08, 0.02)
mpent = makeArray(mpent, 0.9, 0.08, 0.02)
    


#for i in range(size_rhythm):
musicb = GetLine(Bass_beat,I_V,notes, Mpent, mpent, 8)
musicg = GetLine(Guitar_beat,I_V,notes, M7, m7, 20)

import pysynth as pysynth
pysynth.make_wav(musicb, fn="bass.wav")
pysynth.make_wav(musicg, fn="guitar.wav")




