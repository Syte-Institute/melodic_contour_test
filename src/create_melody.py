#### create a audio file with panio sound using given letter notes ####

import re
import fluidsynth
from midiutil import MIDIFile
from pydub import AudioSegment
import os
import json

from utils import note_to_midi


# select melody to create
melody_name = "happy_birthday"

# load data path
with open("path.json") as json_file:
    paths = json.load(json_file)
data_base_path = paths["data"]

# load notes to be played
notes = os.path.join(data_base_path, "notes", f"{melody_name}.txt")

# Load soundfont file
sf2_path = os.path.join(data_base_path, "FluidR3_GM", "FluidR3_GM.sf2")
fs = fluidsynth.Synth()
fs.start(driver="coreaudio")
sf_id = fs.sfload(sf2_path)

# # Set piano instrument as default
piano_program = 0
fs.program_select(0, sf_id, 0, piano_program)

# Parse notes from text file and convert to midi number
with open(notes, "r") as f:
    notes_list = f.read().split()
midi_numbers = note_to_midi(notes_list)

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
for midi_num in midi_numbers:
    midi_file.addNote(track, channel, midi_num, time, duration, volume)
    time += duration

# Create output path if not exists
output_dir = os.path.join(data_base_path, "sound_output")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Write MIDI file to disk
midi_file_path = os.path.join(output_dir, f"{melody_name}.mid")
"output.mid"
with open(midi_file_path, "wb") as f:
    midi_file.writeFile(f)

# Convert MIDI to audio
wav_file_path = os.path.join(output_dir, f"{melody_name}.wav")
cmd = f"fluidsynth -ni {sf2_path} {midi_file_path} -F {wav_file_path} -r 44100"
os.system(cmd)

# Load audio file and play it
audio = AudioSegment.from_wav(wav_file_path)
audio.export(os.path.join(output_dir, f"{melody_name}.mp3"), format="mp3")
