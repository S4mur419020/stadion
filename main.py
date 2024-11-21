from Stadion import Stadion
import filebaolvas
import fladat


stadionok=filebaolvas.beolvas("stadionok.txt", [])
for i in range(0,len(stadionok),1):
    print(stadionok[i])
    
    
db=fladat.newyork(stadionok)
print(f"A New York-i csapatok száma: {db}db")

csdb=fladat.csapatok(stadionok)
print(f"A csapatok száma összesen: {csdb}db")