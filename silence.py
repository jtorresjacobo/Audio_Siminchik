from pydub import AudioSegment
from pydub.playback import play
import wave

###agregando silencio de 0.65 segundos
audio_in_file = "/home/jean/Desktop/Audio_Siminchik/audio/B01___02_San_Mateo___QVETBLN2DA_features.wav"
audio_out_file = "silence.wav"

# create 1 sec of silence audio segment
one_sec_segment = AudioSegment.silent(duration=650)  #duration in milliseconds

#read wav file to an audio segment
song = AudioSegment.from_wav(audio_in_file)

#Add above two audio segments    
final_song = one_sec_segment + song

#Either save modified audio
final_song.export(audio_out_file, format="wav")


#duplicando audio
infiles = [audio_out_file, audio_out_file]
outfile = "sounds.wav"

data= []
for infile in infiles:
    w = wave.open(infile, 'rb')
    data.append( [w.getparams(), w.readframes(w.getnframes())] )
    w.close()

output = wave.open(outfile, 'wb')
output.setparams(data[0][0])
output.writeframes(data[0][1])
output.writeframes(data[1][1])
output.close()