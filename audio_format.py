import os
from time import time

#Parameters
#==========
path = "/home/usuario/Escritorio/test/"

#All type of format can be change to wav
def get_format(archivo,name_file):
	os.system("ffmpeg -i '"+path+archivo+"' -acodec pcm_s16le -ac 1 -ar 16000 '"+path+"audios/"+name_file[0]+".wav'")


#Function principal
def main():
	start_time = time()
	os.system("mkdir "+path+"audios")
	for archivo in os.listdir(carpeta):
		name_file = archivo.split('.')
		get_format(archivo,name_file)
	end_time = time()
	print("time: "+str(end_time-start_time))

if __name__ == "__main__":
	main()