#!/bin/sh
for i in `seq 1 3`; do
    ./grammy.py --depth=4 --length=500 $1 | espeak -p 60 -s 100 -ven+m3 -w voice$i.wav
done

sox voice2.wav tmp.wav pitch 50
mv tmp.wav voice2.wav
sox voice1.wav voice2.wav voice1.wav voice3.wav -r 44100 out.wav delay 3 gain -2
