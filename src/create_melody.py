#!python

import re
from fluidsynth import fluidsynth
from midiutil import MIDIFile
from pydub import AudioSegment
import os

import sys

sys.path.append("/Users/zhoulinn/miniforge3/envs/mci/lib/python3.10/site-packages/")

# Load soundfont file
sf2_path = "FluidR3_GM/FluidR3_GM.sf2"
fs = fluidsynth.Synth()
fs.start(driver="coreaudio")
sf_id = fs.sfload(sf2_path)

# Set piano instrument as default
piano_program = 0
fs.program_select(0, sf_id, piano_program)

# Parse notes from text file
note_pattern = r"([A-G])([0-9])"
with open("notes.txt", "r") as f:
    notes_str = f.read()
notes_list = re.findall(note_pattern, notes_str)

# Set up MIDI file
midi_file = MIDIFile(1)
track = 0
time = 0
tempo = 120
midi_file.addTempo(track, time, tempo)

# Add notes to MIDI file
channel = 0
volume = 100
duration = 1
for note, octave in notes_list:
    pitch = ord(note) - ord("A") + (int(octave) + 1) * 12
    midi_file.addNote(track, channel, pitch, time, duration, volume)
    time += duration

# Write MIDI file to disk
midi_file_path = "output.mid"
with open(midi_file_path, "wb") as f:
    midi_file.writeFile(f)

# Convert MIDI to audio
wav_file_path = "output.wav"
cmd = f"fluidsynth -ni {sf2_path} {midi_file_path} -F {wav_file_path} -r 44100"
os.system(cmd)

# Load audio file and play it
audio = AudioSegment.from_wav(wav_file_path)
audio.export("output.mp3", format="mp3")
