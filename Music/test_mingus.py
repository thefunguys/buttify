from mingus.containers import *
from mingus.containers.instrument import *
from mingus.midi.midi_file_out import *

class Doop(Guitar):
    instrument_nr = 105

notes = [Note("C-3"), Note("Eb-3"), Note("G-3")]
b = Bar()
for note in notes:
    b.place_notes(note, 4)
nc = NoteContainer(["C-3", "Eb-3", "G-3", "C-4"])
b2 = Bar()
b2.place_rest(4)
b2.place_notes(nc, 2)
t = Track(Doop())
t.add_bar(b)
t.add_bar(b2)
mt = MidiTrack()
mt.play_Track(t)

mf = MidiFile([mt])
print mf.get_midi_data()
mf.write_file('test.mid')
