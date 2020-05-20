def read_raw(filename):
    infile = open(filename,"rb")
    indata = infile.read()
    infile.close()
    return indata

def makeString(ASCII_list):
    bdata = bytes(ASCII_list)
    s = bdata.decode("utf-8")
    return s

def decodeFasta(data):
    ou = []
    nameList = []
    proteinList = []
    dataList = []
    collect = "s" #species, protein, data
    for x in data:
        #x is a byte
        if x==32: #space
            if (collect=="s") and (len(nameList)!=0):
                collect = "p"
        elif (x==13) or (x==10): #return
            if (collect=="p") and (len(proteinList)!=0):
                collect = "d"
        elif x==62: # >
            if collect!="d":
                raise Exception("Syntax Error")
            if len(nameList)==0:
                raise Exception("Empty Species Field")
            if len(proteinList)==0:
                raise Exception("Empty Protein Field")
            if len(dataList)==0:
                raise Exception("Empty Data Field")
            ou.append([makeString(nameList),makeString(proteinList),makeString(dataList)])
            nameList = []
            proteinList =[]
            dataList = []
            collect = "s"
        else:
            if collect=="s":
                nameList.append(x)
            elif collect=="p":
                proteinList.append(x)
            elif collect=="d":
                dataList.append(x)
            else:
                raise Exception("Internal coding bug. Please fix.")
    if (len(nameList)!=0) and (len(proteinList)!=0) and (len(dataList)!=0):
        ou.append([makeString(nameList),makeString(proteinList),makeString(dataList)])
    return ou

def merge(oldData,newData):
    #oldData is a dict of dicts
    #newData is a list of tuples
    for x in newData:
        #x is a tuple [species,protein,data]
        #all of them strings
        if x[0] not in oldData: #if you don't know about this species, make it
            oldData[x[0]] = dict()
        oldData[x[0]][x[1]] = x[2]
    #no return

def fasta_parser(list_of_files):
    ou = dict()
    for x in list_of_files:
        rawData = read_raw(x)
        newData = decodeFasta(rawData)
        del(rawData)
        merge(ou,newData)
        del(newData)
    return ou
