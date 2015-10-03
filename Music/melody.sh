#!/bin/sh
python music.py
mv out.wav out1.wav
python music.py
mv out.wav out2.wav
sox out1.wav out2.wav out1.wav out2.wav out2.wav out1.wav out.wav fade t 4 0 4
