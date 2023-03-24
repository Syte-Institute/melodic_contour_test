import librosa

def note_to_midi(note):
    return librosa.note_to_midi(note)

def letter_to_midi(note):
    # note_name = note[1:]
    # octave = int(note[0])
    notes = {
        ".C": -24,
        ".C#": -23,
        ".D": -22,
        ".D#": -21,
        ".E": -20,
        ".F": -19,
        ".F#": -18,
        ".G": -17,
        ".G#": -16,
        ".A": -15,
        ".A#": -14,
        ".B": -13,
        "C": 0,
        "C#": 1,
        "D": 2,
        "D#": 3,
        "E": 4,
        "F": 5,
        "F#": 6,
        "G": 7,
        "G#": 8,
        "A": 9,
        "A#": 10,
        "B": 11,
        "^C": 12,
        "^C#": 13,
        "^D": 14,
        "^D#": 15,
        "^E": 16,
        "^F": 17,
        "^F#": 18,
        "^G": 19,
        "^G#": 20,
        "^A": 21,
        "^A#": 22,
        "^B": 23,
    }
    midi_number = notes[note]
    return midi_number
