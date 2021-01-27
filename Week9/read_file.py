"""
COMP.CS.100 Programming 1
Read genres and tv-series from a file into a dict.
Print a list of the genres in alphabetical order
and list tv-series by given genre on user's command.
"""

def read_file(fileName):
    """
    Read info from csv file and transfer info to a dict of dicts

    :param :fileName-string
    :return : a dict of dicts
    """

    try:
        fileStream = open(fileName,'r')
        infoDict = {}
        firstLine = fileStream.readline()
        keys = firstLine.split(';')
        #print(keys)

        while True:
            line = fileStream.readline()
            if line == '': break

            info = line.split(';')
            #print(info)
            key = info[0]
            infoDict[key] = {}
            n =  len(info)
            
            for i in range(1,len(keys)):
                infoDict[key][keys[i].rstrip()] = info[i].rstrip()
        #print(infoDict)
        return infoDict

    except OSError:
        print("Cannot open file!!!")

#info = read_file("contacts.csv")