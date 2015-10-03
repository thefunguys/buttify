#!/bin/sh
(cd words; ./play.sh albums/am)
(cd Music; ./melody.sh)
sox -m words/out.wav Music/out.wav song.wav
