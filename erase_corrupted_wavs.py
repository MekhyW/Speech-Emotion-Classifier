import wave
import os

corrupted = []

for set in ['test', 'train']:
    for folder in os.listdir(set):
        for file in os.listdir(set+'/'+folder):
            try:
                opened = wave.open(set+'/'+folder+'/'+file, 'rb')
                if opened.getnchannels() != 1:
                    corrupted.append(set+'/'+folder+'/'+file)
                opened.close()
            except:
                corrupted.append(set+'/'+folder+'/'+file)

for path in corrupted:
    os.remove(path)
    print(path+' removed')