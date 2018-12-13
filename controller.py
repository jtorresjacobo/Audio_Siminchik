import utils
import crud



def main(path,user):

	date=utils.date()
	duration=utils.audio_duration(path)

	crud.Insert(user,path,duration,date)





