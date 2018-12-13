import convert_wav_with_features,noise_s,cut,audiospeed
import Extraccion_Fondo
from werkzeug.utils import secure_filename
import os
import espectogrma as spg
import spte_noise
import prue

def audio(file,paths,filenames,user):
      

	file.save(os.path.join(paths,filenames))

	#convert to format wav with features 
	#"name " is the name of audio file 
	name=convert_wav_with_features.audio(paths,filenames,user)

	#modify audio speed to 0.5
	audiospeed.input_pathaudio(paths,name,user)

	#separating audio every 30 seconds
	cut.separate_audio(paths,name,user)

	#noise
	noise_s.path(paths,name,user)

	#fondo
	fil=Extraccion_Fondo.Extrac_Sonido(paths,filenames,user)

	#sin fondo
	spte_noise.audioclean(paths,name,fil,user)

	#Espectograma
	spg.plotstft(paths+"/"+name)

	#Estadisticas
	prue.statictis(name,paths)
	prue.statictis(filenames,paths)
