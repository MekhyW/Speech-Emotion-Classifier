import wave
import os
import tensorflow as tf

corrupted = []

for set in ['test', 'train']:
    for folder in os.listdir(set):
        for file in os.listdir(set+'/'+folder):
            path = set+'/'+folder+'/'+file
            if os.path.getsize(path) == 0 or not file.endswith('.wav'):
                corrupted.append(path)
            else:
                try:
                    opened = wave.open(path, 'rb')
                    if opened.getnchannels() != 1:
                        corrupted.append(path)
                    opened.close()
                    input_data = tf.io.read_file(path)
                    audio, sampling_rate = tf.audio.decode_wav(input_data)
                except:
                    corrupted.append(path)

for path in corrupted:
    os.remove(path)
    print(path+' removed')
print(len(corrupted), 'files removed')