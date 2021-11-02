from midiutil.MidiFile import MIDIFile
# pip3 install midiutil

# Author: https://github.com/0xturazzi

# Having both notes and note.subs is redundant
# But it will be useful for note deletion if I decide to make a GUI

class Note:
    def __init__(self, time, duration):
        self.sub = [] # keeps track of the index of it's child notes on the main notes array
        self.time = time
        self.duration = duration

    def divide(self, divs):
        if divs == 1:
            return

        global notes
        self.sub = [] # clearing it will allow interactively changing the tuple on the UI w/o trouble
        time = self.time
        duration = self.duration / divs # if needed, precision can be increased using decimal
        for i in range(divs):
            self.sub.append(len(notes)) 
            notes.append(Note(time, duration))
            time += duration
        return len(notes) - divs

    def delete(self):
        self.sub = [1]

def save(notes):
    mf = MIDIFile(1) # 1 track
    track = 0
    time = 0
    mf.addTrackName(track, time, name)
    mf.addTempo(track, time, 120)

    pitch = 67
    channel = 0
    volume = 100

    for note in notes: 
        if note.sub: continue # Prevent Overlap from parent note
        
        time = note.time
        duration = note.duration
        mf.addNote(track, channel, pitch, time, duration, volume)

    with open(f"{name}.mid", 'wb') as outfile:
        mf.writeFile(outfile)

##########################################################
# Config
name = "GeneratedTuples"
start_size = 4 # Measured in Beats
##########################################################
# Edit Area
notes = [Note(0, start_size)]
notes[0].divide(3) 
notes[1].divide(7) 
notes[2].divide(3)
notes[3].divide(5) 
##########################################################
######### Procedural Generation Example
# notes = []
# from random import randint
# for i in range(10):
#     a = len(notes)
#     notes.append(Note(i*start_size, start_size))
# 
#     a = notes[a].divide(5) 
#     notes[a].divide(randint(1,4)) 
#     notes[a+1].delete()
#     notes[a+2].delete() 
#     notes[a+3].divide(randint(1,4)) 
#     notes[a+4].divide(randint(1,4)) 
##########################################################
save(notes)
