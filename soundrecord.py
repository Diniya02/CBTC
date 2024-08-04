import sounddevice as sd
import wavio
import numpy as np

samplerate = 44100  # Hz
duration = 10  # seconds
filename = 'recording.wav'

# Record audio
print('Recording...')
myrecording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2, blocking=True)
print('Recording finished.')

# Save the recorded audio as a WAV file
wavio.write(filename, myrecording, samplerate, sampwidth=2)

# Play the recorded audio
print('Playing recording...')
sd.play(myrecording, samplerate)
sd.wait()
print('Playback finished.')