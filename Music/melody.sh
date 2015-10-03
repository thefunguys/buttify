#!/bin/sh
python music.py
mv out.wav out1.wav
python music.py
mv out.wav out2.wav
sox out1.wav out2.wav out1.wav out1.wav out2.wav out2.wav out1.wav out1.wav out2.wav out2.wav out1.wav out1.wav out.wav fade t 4 0 4
sox bass.wav newbass.wav gain +8
sox -m newbass.wav out.wav final.wav
