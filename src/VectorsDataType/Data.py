def Vars(vec):
    l = list(vec.keys())
    for point in l:
        i=0
        while i < len(vec[point]):
            
            globals()[point+str(i)]=vec[point][i]
            j=0
            while j < len(vec[point][i]):
                globals()[point+str(i)+str(j)] =vec[point][i][j]
                j+=1
            i+=1
g = globals()
def Update():
    g = globals()