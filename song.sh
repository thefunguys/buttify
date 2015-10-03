#!/bin/sh
(cd words; ./play.sh albums/$1)
(cd Music; ./melody.sh)
sox -m words/out.wav Music/final.wav static/song.wav
