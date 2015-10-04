#!/bin/bash
python real_music.py

triml=16

for file in bassb basse guitar
do
    sox $file.wav ${file}_t.wav trim 0 $triml

done

sox bassb_t.wav basse_t.wav newbass1.wav gain +14
sox guitar_t.wav newguitar1.wav overdrive vol 0.25 
sox -m r1.wav r3.wav r7.wav rhythm.wav

echo "First Read"

rm bass*
rm guitar*

python real_music.py

for file in bassb basse guitar
do
    sox $file.wav ${file}_t.wav trim 0 $triml

done

sox bassb_t.wav basse_t.wav newbass2.wav gain +14
sox guitar_t.wav newguitar2.wav overdrive vol 0.25

rm bass*
rm guitar*

sox silence.wav newguitar0.wav trim 0 $triml

echo "Second Read"

if [[ $(( $RANDOM % 2 )) == 0 ]]; then
    VERSE_PAT=1122
else
    VERSE_PAT=1212
fi

if [[ $(( $RANDOM % 2 )) == 0 ]]; then
    CHORUS_PAT=1122
else
    CHORUS_PAT=1100
fi

END_PAT=1

PAT_FACTOR=$(( $RANDOM % 3 ))
if [[ $PAT_FACTOR == 0 ]]; then
    OVERALL_PAT=vcvc
elif [[ $PAT_FACTOR == 1 ]]; then
    OVERALL_PAT=vcvcc
else
    OVERALL_PAT=vvcv
fi

sox newbass1.wav newbass2.wav bassline.wav
sox rhythm.wav rhythm.wav rhythm.wav rhythm.wav fullrhythm.wav

echo "Bass and rhythm set up"

sox newguitar${VERSE_PAT:0:1}.wav newguitar${VERSE_PAT:1:1}.wav newguitar${VERSE_PAT:2:1}.wav newguitar${VERSE_PAT:3:1}.wav preverse.wav

sox newguitar${CHORUS_PAT:0:1}.wav newguitar${CHORUS_PAT:1:1}.wav newguitar${CHORUS_PAT:2:1}.wav newguitar${CHORUS_PAT:3:1}.wav prechorus.wav

echo "chorus and verse started"

sox -m bassline.wav fullrhythm.wav preverse.wav verse.wav
sox -m bassline.wav fullrhythm.wav prechorus.wav chorus.wav

echo "finished"

sox verse.wav tmp1.wav

i=1
while [ $i -lt ${#OVERALL_PAT} ]
do
    let j=$i+1
    if [ ${OVERALL_PAT:$i:1} = "v" ]
    then
	echo v
	sox tmp${i}.wav verse.wav tmp${j}.wav
	
    else
	echo c
	sox tmp${i}.wav chorus.wav tmp${j}.wav
    fi
    i=$((i+1))
done

sox tmp4.wav song.wav
rm tmp*
rm r*.wav



