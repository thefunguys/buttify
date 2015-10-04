#!/bin/sh
python real_music.py

sox bass.wav newbass.wav
sox guitar.wav newguitar.wav overdrive
sox -m r1.wav r3.wav r7.wav rhythm.wav 
cp rhythm.wav ../static/ 
cp newguitar.wav ../static/
sox -m newbass.wav newguitar.wav rhythm.wav final.wav fade 2 0 2
