# Getting started

## Install FluidSynth 
For example, install using homebrew:
```brew install fluidsynth```

## Setup

1. Clone repository \
```git clone https://github.com/Syte-Institute/melodic_contour_test.git``` \
```cd melodic_contour_test```

2. Create virtual environment with Python version 3.10 (for example using Conda) \
```conda create --name name_of_your_choice python=3.10``` \
```conda activate name_of_your_choice```

3. Install requirements \
```conda install --file requirements.txt```

Alternatively, skip steps 2 and 3, create conda environment with .yml file:
```conda env create -f environment.yml```


### Fix ImportError: Couldn't find the FluidSynth library.
If you get "ImportError: Couldn't find the FluidSynth library." while importing fluidsynth, it is probably because the find_library method couldn't find the fluidsynth library in homebrew dictionary.

To fix this, do the following (see https://stackoverflow.com/questions/62478717/importerrorcouldnt-find-the-fluidsynth-library):

1. Find the path of fluidsynth. In terminal, run ```brew --prefix fluidsynth```
My result is ```/opt/homebrew/opt/fluid-synth``` 
The path of fluidsynth then would be ```/opt/homebrew/opt/fluid-synth/lib/libfluidsynth.dylib```, copy this path.
2. Open the "fluidsynth.py" file that is being imported (the path is displayed in the error message), e.g., at ```/Users/miniforge3/envs/pyfluidsynth/lib/python3.10/site-packages/```.
3. In the editor, find the lines
```
    lib = (
        find_library("fluidsynth")
        or find_library("libfluidsynth")
        or find_library("libfluidsynth-1")
        or find_library("libfluidsynth-1.dll")  
    )
```
After that line, add a new line lib = ```<path>``` with the path from step 1.


### Fix fluidsynth: error: Unknown integer parameter 'synth.sample-rate'
1. Open the "fluidsynth.py" file that is being imported
2. Go to ```class Synth```
3. Change the default ```samplerate=44100``` into ```samplerate=44100.0```
