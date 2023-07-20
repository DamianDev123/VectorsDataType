
def ToVector3(v):
    vs = v.split(" ")
    v3 = []
    
    for v in vs:
        try:
            i = int(v)
            v3.append(i)
        except:
            pass
        
    return v3
def Vector3(x,y,z):
    return {"x":x,"y":y,"z":z}
def ReadFile(name):
    segment = ""
    points = {}
    i = 0
    f = open(name,"r")
    lines = f.readlines()
    while i < len(lines):  
        if lines[i][0].__contains__("#"):
            i+=1
        if lines[i][0].__contains__("?"):
            segment = lines[i][1:]
            segment = segment[:len(segment)-1]
            points[segment] = []
            i+=1
        points[segment].append(ToVector3(lines[i]))
        i+=1
        
    f.close()
    return points;
