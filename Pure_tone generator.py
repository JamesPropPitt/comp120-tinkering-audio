import wave
import struct
import math

# Sound made
noise_output = wave.open('Pure_tone', 'w')

# Sets the numbers for the parameters
frequency = 220
sampleRate = 44100
sampleLength = sampleRate*3
volume = 1
bitDepth = 32767
soundTuple = (2, 2, sampleRate, sampleLength, 'NONE', 'not compressed')

# Sets the parameters to the sound made
noise_output.setparams(soundTuple)

# For the length of the sound sample, i denotes what the wave value is at certain times
for i in range(0, sampleLength):
   value = math.sin(2.0 * math.pi * frequency * ( i / float(sampleRate))) * (volume * bitDepth)
   print value
   packed_value = struct.pack('h', value)
   noise_output.writeframes(packed_value)
   noise_output.writeframes(packed_value)

noise_output.close()
