path="database2.txt"
def LuuFile(line):
    try:
        file = open(path, 'a', encoding='utf-8')
        file.writelines(line)
        file.writelines("\n")
        file.close()
    except:
        pass

def DocFile():
    arrsach=[]
    try:
        file = open(path, 'r', encoding="utf-8")
        for line in file:
            data = line.strip()
            array= data.split(";")
            arrsach.append(array)
        file.close()
    except:
        pass
    return arrsach
