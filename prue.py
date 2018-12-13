import os
import commands

def statictis(name,path):

    name_file=name.split('.')
    stat1=commands.getstatusoutput('sox --i '+path+'/'+name )
    stat2=commands.getstatusoutput("sox "+path+'/'+name+"  -n stat")
    f=open("fichero_"+name_file[0]+"-stat.txt","w")
    f.write(stat1[1])
    f.write('\n')
    f.write(stat2[1])
    f.close()
    print(path+name)
  
