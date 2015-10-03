#!/bin/sh
python real_music.py

sox bass.wav newbass.wav gain +8
sox -m newbass.wav guitar.wav final.wav fade 4 0 4
