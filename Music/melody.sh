#!/bin/sh
python real_music.py

sox bass.wav newbass1.wav gain +6
sox guitar.wav newguitar1.wav overdrive gain -10
sox -m r1.wav r3.wav r7.wav rhythm.wav gain +10
python real_music.py

sox bass.wav newbass2.wav gain +6
sox guitar.wav newguitar2.wav overdrive gain -10

cp rhythm.wav ../static/ 
cp newguitar.wav ../static/
if [[$(($RANDOM % 2)) == 0]]; then
    VERSE_PAT=1122
else
    VERSE_PAT=1212
fi

if [[$(($RANDOM % 2)) == 0]]; then
    CHORUS_PAT=1122
else
    CHORUS_PAT=1100
fi

END_PAT=1

PAT_FACTOR=$(($RANDOM % 2))
if [[PAT_FACTOR == 0]]; then
    OVERALL_PAT=vcvc
elif 
    OVERALL_PAT=vcvcc
else
    OVERALL_PAT=vvcv
fi

sox newguitar${VERSE_PAT:0:1}.wav newguitar${VERSE_PAT:1:1}.wav newguitar${VERSE_PAT:2:1}.wav newguitar${VERSE_PAT:3:1}.wav verse.wav

sox newguitar${CHORUS_PAT:0:1}.wav newguitar${CHORUS_PAT:1:1}.wav newguitar${CHORUS_PAT:2:1}.wav newguitar${CHORUS_PAT:3:1}.wav chorus.wav


