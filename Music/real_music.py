import random
from datetime import datetime

random.seed(datetime.now())


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

def GetMelody(beat,prog,notes,M, m, bottom):
    music = []
    prevnote = 0
    prevtype = 1

    Mmod= list(M)
    mmod = list(m)
    Mmod[0] = Mmod[0]+1
    mmod[0] = mmod[0]+1
    Mmodp = makeArray(Mmod,0.85, 0.1, 0.05)
    mmodp = makeArray(mmod,0.85, 0.1, 0.05)

    for k in prog:
        for rhy_pat in beat:
            for j in rhy_pat:
                val = 0
                condition = 0
                if prevtype == 1:
                    condition = 2
                elif prevtype != 1:
                    condition = 4
                else:
                    condition = 10
                    
                if j != 0:
                    if k == 10:
                        val = getNote(changeArray(mmod, condition,prevnote , mmodp))
                        prevtype = mmod[val-1]
                    else:
                        val = getNote(changeArray(Mmod, condition, prevnote, Mmodp))
                        prevtype = Mmod[val-1]
                    prevnote = val
                    
                    letter = notes[val + bottom + k - 1]
                else:
                    letter = 'r'
                    j=16
                music.append([letter, j])
        
    return music

def changeArray(scalenotes, condition,note_played, probsgiven):
    #conditions are:
    # 1 = note is 16, so want to move
    # 2 = note is a 1 want to stay
    # 4 = note is a 2 want to move
    # 3, 5 =  2 and 4 with condition 1 as well
    probsA = list(probsgiven)
    prob = 0.3
    reduc = 1. - prob
    size = len(probsA)

    for i in range(size):
        probsA[i] = probsA[i]*reduc

    if condition == 2:
        for i in range(size-note_played):
            probsA[note_played + i] = probsA[note_played + i] + prob
    
    elif condition == 4:
        for i in range(2):
            if note_played-i-1 >=0 and scalenotes[note_played-i-1]==1:
                for j in range(size - (note_played-i-1)):
                    probsA[note_played-i-1+j] = probsA[note_played-i-1+j] + prob/2.

            if note_played+i+1 <size and scalenotes[note_played+i+1]==1:
                for j in range(size - (note_played+i+1)):
                    probsA[note_played+i+1] = probsA[note_played+i+1] + prob/2.
    
    else:
        return probsgiven
    #print "test"
    #print probsA



#    elif condition == 1:
#        if note_played-1 >=0:
#            probsA[note_played-1] = probsA[note_played-1] + prob/2.
#
#        if note_played+i+1 < size:
#            probsA[note_played+1] = probsA[note_played+1] + prob/2.
#
        
    return probsA




def makeArray(ns, pgood, pok, pbad):
    Notes = list(ns)
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
        x = random.randint(0,len(Array)-1)
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
                    j=8
                    
                music.append([letter,j])
        
    return music




notes = readNotes()

the_progs = []

the_progs.append([1,8,10,6])
the_progs.append([10,6,1,8])
the_progs.append([6,1,8,10])



guitar_rhy = []
guitar_rhy.append([8,8,8,8,8,8,8,8])
guitar_rhy.append([8,16,16,16,16,16,16,16,16,8,4])
guitar_rhy.append([8,16,8,16,-8,16,8,8,16,16])
guitar_rhy.append([-8,16,16,16,16,8,8,16,16,16,8])
guitar_rhy.append([-8,-8,4,8,4])
guitar_rhy.append([-8,-8,-8,-8,16,-8])


bass_rhy = []
bass_rhy.append([8,8,8,8])
bass_rhy.append([8,8,-8,16])
bass_rhy.append([8,4,8])
bass_rhy.append([4,4])
bass_rhy.append([2])
bass_rhy.append([-4,8])

r_rhy = []
r_rhy.append([8,8,8,8,8,8,8,8])
r_rhy.append([8,8,8,8,0,8,8,8])
r_rhy.append([0,8,8,8,0,8,8,8])
r_rhy.append([8,8,8,-4,0,8])

Bass_beat = []
Bass_beat2 = []
bass_size = 4
Guitar_beat = []
guitar_size = 2
Rhythm_beat = []
r_size = 2

picks = pickBeat(bass_rhy,bass_size)
for i in range(bass_size):
    Bass_beat.append(bass_rhy[picks[i]])

picks = pickBeat(bass_rhy,bass_size)
for i in range(bass_size):
    Bass_beat2.append(bass_rhy[picks[i]])
    
picks = pickBeat(guitar_rhy,guitar_size)
for i in range(guitar_size):
    Guitar_beat.append(guitar_rhy[picks[i]])

picks = pickBeat(r_rhy,r_size)
for i in range(r_size):
    Rhythm_beat.append(r_rhy[picks[i]])


    
M7g = makeArray(M7, 0.75, 0.2, 0.05)
m7g = makeArray(m7, 0.75, 0.2, 0.05)
Mpentb = makeArray(Mpent, 0.9, 0.08, 0.02)
mpentb = makeArray(mpent, 0.9, 0.08, 0.02)
n1 = [1,1,1,1,1,1,1,1,1,1,1,1,1]
nM3 = [0,0,0,0,1,1,1,1,1,1,1,1,1]
nM7 = [0,0,0,0,0,0,0,0,0,0,0,1,1]
nm3 = [0,0,0,1,1,1,1,1,1,1,1,1,1]
nm7 = [0,0,0,0,0,0,0,0,0,0,1,1,1]


pick_prog = the_progs[random.randint(0,len(the_progs)-1)]

#for i in range(size_rhythm):
musicb = GetLine(Bass_beat,pick_prog,notes, Mpentb, mpentb, 8)
musicb2 = GetLine(Bass_beat2,pick_prog,notes, Mpentb, mpentb, 8)
musicg = GetMelody(Guitar_beat,pick_prog,notes, M7, m7, 32)
r1 = GetLine(Rhythm_beat, pick_prog, notes, n1, n1, 20)
r3 = GetLine(Rhythm_beat, pick_prog, notes, nM3, nm3, 20)
r7 = GetLine(Rhythm_beat, pick_prog, notes, nM7, nm7, 20)

import pysynth as A_synth
import pysynth_b as B_synth
import pysynth_e as E_synth

B_synth.make_wav(musicb, fn="bassb.wav", bpm=120)
B_synth.make_wav(musicb2, fn="basse.wav", bpm=120)
E_synth.make_wav(musicg, fn="guitar.wav", bpm=120)
A_synth.make_wav(r1, fn="r1.wav", bpm=120)
A_synth.make_wav(r3, fn="r3.wav", bpm=120)
A_synth.make_wav(r7, fn="r7.wav", bpm=120)
##




