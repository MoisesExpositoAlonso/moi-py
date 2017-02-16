## A LIBRARY MEANT FOR MOI'S DAILY PROGRAMMING 
import os, sys, time, datetime



def getfilenames(included_extenstions,relevant_path):
    file_names = [fn for fn in os.listdir(relevant_path)
        if any(fn.endswith(ext) for ext in included_extenstions)]
    return  file_names

def parsealltimes(file_names):
    alltimes=[]
    for fil in file_names:
        (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(fil)
        # print "last modified: %s" % time.ctime(mtime)
        parsedtime=time.strftime("%Y_%m_%d", time.gmtime(mtime))
        print time.strftime("%Y_%m_%d", time.gmtime(mtime))
        alltimes.append(parsedtime)
    return alltimes

def makefolders(uniquedates):
    for x in uniquedates:
        print x
        if not os.path.exists(x):
            os.makedirs(x)

def renameinfolders(file_names,alltimes):
    for (myfile,mydate) in zip(file_names,alltimes):
        print myfile, mydate
        targetfolder= [x for x in uniquedates if x == mydate]
        print "this is target folder: %s" %(targetfolder)
        newname=str(mydate+"/"+myfile)
        print newname
        os.rename(myfile,newname)


def monitor_successfiles(foldername, filenames=None, time_wait='1h', time_max='48h'):
    '''Monitor the presence of success files in a folder
    
    Parameters:
      time_max (int or str): if int, max number of seconds to wait. If string, it
      has to be something like '48h', which is then converted into seconds.
    '''
    def convert_timetring(time):
        if isinstance(time, basestring):
            unit = time[-1]
            if unit == 'h':
                factor = 3600
            elif unit == 'm':
                factor = 60
            elif unit == 's':
                factor = 1
            else:
                raise ValueError('Time unit not understood')
            time = int(time[:-1]) * factor
        return int(time)


    def clean_foldername(foldername):
        import os
        return foldername.rstrip(os.sep)+os.sep


    def clean_filename(foldername):
        import os
        return foldername.lstrip(os.sep)


    def check_single_file(filename):
        '''Check existance of single file'''
        import os.path
        return os.path.isfile(filename)

    # Get input time parameters
    time_wait = convert_timetring(time_wait)
    time_max = convert_timetring(time_max)

    # Get the foldername paramter
    foldername = clean_foldername(foldername)

    # Get the filenames parameters, relative to the foldername
    if filenames is None:
        import os
        filenames = os.listdir(foldername)
    # NOTE: Transform into absolute paths
    filenames_abs = [foldername+clean_filename(fn) for fn in filenames]

    # Monitor files
    import time
    t = 0
    while t < time_max:
        if all(map(check_single_file, filenames_abs)):
            break
        time.sleep(time_wait)
        t += time_wait
    else:
        return 'Maximal time reached'

    return 'OK'



def readtabtable(filename):
	table=open( filename,"r")
	cleanedtable=[x.replace("\n","").split("\t") for x in table]
	return cleanedtable


def listostring(list1):
# you have sth like ['A'] you get 'A'
    return str(list1).replace('[','').replace(']','').replace("'",'')



def findmostcommon(word):
# you have a string like 'AAAACAAAA' you get the most common letter, A as a 'A' string
    word=listostring(word)
    acceptedbases=["A",
               "G",
               "C",
               "T"]
    
    ase=word.count('A')
    ges=word.count('G')
    ces=word.count('C')
    tes=word.count('T')
    countings=[ase,ges,ces,tes]
    dictio={}
    for k, v in zip(acceptedbases, countings):
        dictio[k] = v
 
    mostcommon=list(base for base in dictio if dictio[base]==max(countings))
    return listostring(mostcommon)


def findleastcommon(word):
# you have a string like 'AAAACAAAA' you get the most common letter, A as a 'A' string
	word=listostring(word)
	acceptedbases=["A","G","C","T"]
	ase=word.count('A')
	ges=word.count('G')
	ces=word.count('C')
	tes=word.count('T')
	countings=[ase,ges,ces,tes]
	dictio={}
	for k, v in zip(acceptedbases, countings):
		dictio[k] = v
	leastcommon=list(base for base in dictio if dictio[base]>min(countings) and dictio[base]!=max(countings))
	return listostring(leastcommon)


def combinations(iterable, r):
#combinations('ABCD',2)-->ABACADBCBDCD
#combinations(range(4),3)-->012013023123
	pool=tuple(iterable)
	n=len(pool)
	if r>n:
		return
	indices=range(r)
	yield tuple(pool[i] for i in indices)
	while True:
		for i in reversed(range(r)):
			if indices[i] != i+n-r:
				break
		else:
			return
		indices[i]+=1
		for j in range(i+1,r):
			indices[j]=indices[j-1]+1
		yield tuple (pool[i] for i in indices)

