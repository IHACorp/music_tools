from midiutil.MidiFile import MIDIFile
# pip3 install midiutil
from random import randint

# Author: https://github.com/0xturazzi

class Pattern:
    def __init__(self, positions, acc, can_random_acc, weight, rep_weight, can_rep, density, complexity, timesig, can_expire, expire_after, speed):
        self.positions = positions # 1 to 4 Ex: [1,   1.75, 3,   3.5]
        self.acc = acc # Volumes            Ex" [200, 100,  200, 100]
        self.can_random_acc = can_random_acc * (len(acc) != len(positions)) # Bool
        self.weight = weight # 0-1
        self.can_rep = can_rep # bool
        self.rep_weight = rep_weight * (can_rep > 0) # 0-1
        self.density = density # in straight 4/4 : 
                               # |0 whole 
                               # |1 half/4th 
                               # |2 8th 
                               # |3 8thtri 
                               # |4 16th 
                               # |5  <16th 
        self.complexity = complexity # |0 straight  
                                     # |1 swing/unquantized 
                                     # |2 sincopated 
                                     # |3 simple tuplets / polyrithms 
                                     # |4 weird tuplets / polyrithms 
                                     # |5 nested tuplets
        self.timesig = timesig # (x,y) : (4,4) (3,4)
        self.can_expire = can_expire # bool
        self.expire_after = expire_after # Number Of non rep uses
        self.speed = speed # |0 <50 
                           # |1 50-90 
                           # |2 90-120 
                           # |3 120-140 
                           # |4 140-180 
                           # |5 180+
        self.

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
base_name = "Pattern_Mixer"
pattern_size = 4 # Measured in Beats
number_pat = 300
speed = (1,2,3)
density = (1,4,5)
complexity = (2,5)
alternate_diff = True
               # True = Alternate Diff 
               # False = Group Similar
timesig = (4,4)

##########################################################
##########################################################
##########################################################
