import wave, struct, math
# Sample rate
samprate = 44100
# Open wav. files
values = []
noise_a = wave.open('cat_y.wav', 'w')
noise_b = wave.open('sound4_2.wav', 'w')

noise_a.setnchannels(1)
noise_a.setsampwidth(2)
noise_a.setframerate(samprate)
aframes = noise_a.setnframes(44100 * 100)
noise_a.setcomptype('NONE', 'not compressed')
noise_a.getparams()
frequency = 300

print noise_a.getparams()

noise_b.setnchannels(1)
noise_b.setsampwidth(2)
noise_b.setframerate(samprate)
bframes = noise_b.setnframes(44100 * 100)
noise_b.setcomptype('NONE', 'not compressed')
noise_b.getparams()
print noise_b.getparams()


# sound algorithm
for i in range (0, 44100):
    sound1 = math.sin(2.0 * math.pi * frequency * (i / 44100.0)) * (0.5 * (2**15-1))
    print sound1
    data = struct.pack("<h", sound1)
    frequency += 90
    for j in xrange (0, 1):
        values.append(data)
# sound2 algorithm
for i in range (0, 44100):
    sound2 = math.sin(2.0 * math.pi * frequency * (i / 44100.0)) * (0.5 * (2**15-1))
    print sound2
    data = struct.pack("<h", sound2)
    frequency += 3
    for j in xrange (0, 1):
        values.append(data)


sound2_str = ''.join(values)
noise_a.writeframes(sound2_str)
noise_a.close()
sound1_str = ''.join(values)
noise_b.writeframes(sound1_str)
noise_b.close()

