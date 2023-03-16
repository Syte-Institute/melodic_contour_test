from pysynth import make_wav

# define the melody as a list of tuples, where each tuple is a note and its duration
melody = [("A4", 4), ("B4", 4), ("C5", 4), ("D5", 4), ("E5", 4), ("F5", 4), ("G5", 4), ("A5", 4)]

# generate the audio samples for the melody using the built-in "piano" sound
audio_data = make_wav(melody, fn = "piano")

# write the audio data to a WAV file
with open("melody.wav", "wb") as f:
    f.write(audio_data)