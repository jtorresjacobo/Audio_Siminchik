import convert_wav_with_features,noise_s,cut,audiospeed,silencio,duplicado_audio
import Extraccion_Fondo
from werkzeug.utils import secure_filename
import os
import espectogrma as spg
import spte_noise
import prue

def audio(file,paths,filenames,user):

	#file: archivo ingresado 
	#paths: ruta a almacenar los audios procesados
	#filenames: nombre del archivo ingresado

    #Guarda audio original en la ruta ./audio
	file.save(os.path.join(paths,filenames))

	#Convierte cualquier audio en formato .wav / name es el nombre del archivo convertido .wav 
	name=convert_wav_with_features.audio(paths,filenames,user)

	#Disminuye la velocidad del audio a 0.5 de la actual
	audiospeed.input_pathaudio(paths,name,user)

	#Separa el audio cada 30 segundos
	cut.separate_audio(paths,name,user)

	#Agrega ruido al audio
	noise_s.path(paths,name,user)

	#agregando silencio de 0.65s
	s_audio=silencio.agregar(paths,name)

	#duplicando audio
	duplicado_audio.execute(paths,s_audio)

	#Extrae el fondo del audio --- proceso necesario para la limpieza del audio
	fil=Extraccion_Fondo.Extrac_Sonido(paths,filenames,user)

	#Audio limpio, recorta vacios, disminuye ruidos 
	spte_noise.audioclean(paths,name,fil,user)

	#Genera espectogramas
	spg.plotstft(paths+"/"+name)

	#Estadisticas
	prue.statictis(name,paths)
	prue.statictis(filenames,paths)
