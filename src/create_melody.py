#### create a audio file with panio sound using given letter notes ####

import re
import fluidsynth
from midiutil import MIDIFile
from pydub import AudioSegment
import os
import json


def make_melody(data_base_path, melody_name):
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

    # Parse notes from text file
    note_pattern = r"[A-G](?:[0-9])?"
    with open(notes, "r") as f:
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
    midi_file_path = os.path.join(data_base_path, "sound_output", f"{melody_name}.mid")
    "output.mid"
    with open(midi_file_path, "wb") as f:
        midi_file.writeFile(f)

    # Convert MIDI to audio
    wav_file_path = os.path.join(data_base_path, "sound_output", f"{melody_name}.wav")
    cmd = f"fluidsynth -ni {sf2_path} {midi_file_path} -F {wav_file_path} -r 44100"
    os.system(cmd)

    # Load audio file and play it
    audio = AudioSegment.from_wav(wav_file_path)
    audio.export(
        os.path.join(data_base_path, "sound_output", f"{melody_name}.mp3"), format="mp3"
    )


if __name__ == "__main__":

    # load data path
    with open("path.json") as json_file:
        paths = json.load(json_file)
    data_base_path = paths["data"]

    for melody_name in ["rise_fall", "rise", "fall"]:
        make_melody(data_base_path, melody_name)
