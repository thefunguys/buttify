#!/bin/sh
./grammy.py --depth=4 --length=1000 $1 | espeak -s 100 -w voice.wav
sox voice.wav -r 44100 out.wav delay 3
