import wave
import struct

#wavefile = wave.open('noise2.wav', 'r')
#numaudioframes = wavefile.getnframes()

#params = wavefile.getparams()

#for i in range(0, numaudioframes):
 #  wavedata = wavefile.readframes(1)
  # data = struct.unpack("<h", wavedata)
   #print(int(data[0]))

#print params

sound_out = wave.open('soundtest', 'w')
sound_out.setparams(1, 1, 44100, 60, None)

for i in range(0, SAMPLE_LEN):
    






sound_out.writeframes()