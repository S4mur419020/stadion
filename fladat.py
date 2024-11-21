def newyork(stadion_lista):
    db=0
    for i in range(0,len(stadion_lista),1):
        if stadion_lista[i].varos=="New York":
            db+=1
    return db

def csapatok(stadion_lista):
    csdb=0
    for i in range(0,len(stadion_lista),1):
        if 1<= stadion_lista[i].csapatok_szama <=100:
            csdb+=1
    return csdb