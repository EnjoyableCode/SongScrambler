import subprocess
from multiprocessing import Process
from random import randint
import random
import re

from notes import *

lilypond_dir = '../../../../lilypond/usr/bin/lilypond'
timidity_dir = '/usr/bin/timidity'





def scramble_notes(old_notes):

    if '|' not in old_notes:
        return old_notes

    notes_split = old_notes.split('\n')

    pipelines = []
    notelines = []
    temp = ''
    for index, ns in enumerate(notes_split):
        if '| %' in ns:
            pipelines.append(ns)
            notelines.append(temp)
            temp = ''
        else:
            temp = temp + ns

    random.shuffle(notelines)

    new_notes = ''
    for index, n in enumerate(notelines):
        new_notes = new_notes + '\n' + n
        if n >= len(pipelines):
            new_notes = new_notes + '\n' + pipelines[index]

    return new_notes


    

randno = random.randint(0,len(notes_to_pick) - 1)

new_notes = notes_to_pick[randno]

new_notes = scramble_notes(new_notes)

randno2 = random.randint(0,len(notes_to_pick) - 1)

new_notes2 = notes_to_pick[randno2]

new_notes2 = scramble_notes(new_notes2)

randno3 = random.randint(0,len(notes_to_pick) - 1)

new_notes3 = notes_to_pick[randno3]

new_notes3 = scramble_notes(new_notes3)

randno = random.randint(0,len(insts) - 1)
new_inst1 = insts[randno]

randno = random.randint(0,len(insts) - 1)
new_inst2 = insts[randno]

randno = random.randint(0,len(insts) - 1)
new_inst3 = insts[randno]

with open('base_music.ly', 'rb') as f:
    data = f.read()
    new_data = data.replace('|||PUTNOTESHERE1|||', new_notes)
    new_data = new_data.replace('|||PUTNOTESHERE2|||', new_notes2)
    new_data = new_data.replace('|||PUTNOTESHERE3|||', new_notes3)
    new_data = new_data.replace('|||PUTINST1HERE|||', new_inst1)
    new_data = new_data.replace('|||PUTINST2HERE|||', new_inst2)
    new_data = new_data.replace('|||PUTINST3HERE|||', new_inst3)
with open('newsong.ly', 'wb') as f:
    f.write(new_data)
subprocess.call([lilypond_dir, 'newsong.ly'])
subprocess.call(['/usr/bin/timidity', 'newsong.midi'])  


