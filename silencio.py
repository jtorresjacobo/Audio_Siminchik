# -*- coding: utf-8 -*- 
from pydub import AudioSegment
from pydub.playback import play

###agregando silencio de 0.65 segundos
def agregar(paths,name):
	audio_in_file = paths+"/"+name
	names="silence_"+name
	audio_out_file = paths+"/"+names


	# create 1 sec of silence audio segment
	one_sec_segment = AudioSegment.silent(duration=650)  #duración en milisegundos

	#read wav file to an audio segment
	song = AudioSegment.from_wav(audio_in_file)

	#Add above two audio segments    
	final_song = one_sec_segment + song

	#Either save modified audio
	final_song.export(audio_out_file, format="wav")

	return names
