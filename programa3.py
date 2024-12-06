print("----------------Programa 3----------------")
print("")
print("Atspekite valstybes sostinę")
vardas=str(input("Įveskite savo vardą -> "))
with open ("rezultatai3.txt", "r") as rf:
    zaideju_kiekis=len(rf.readlines())
visi_zaidejai={}
with open ("rezultatai3.txt", "r") as rf:
    for i in range (zaideju_kiekis):
        line=list(map(str, rf.readline().strip().split()))
        visi_zaidejai[line[0]]=int(line[2])
        
import random
with open ("duomenys3.txt", "r") as df:
    alllines=df.readlines()
    ilgis=len(alllines)
with open ("duomenys3.txt", "r") as df:
    miestai={}
    for i in range(ilgis):
        line=list(map(str, df.readline().strip().split()))
        miestai[line[0]]=line[1]
    df.close()
naudoti=[]
spejimai=0
atspeti=0
for i in range(ilgis):
    while True:
        salis, miestas = random.choice(list(miestai.items()))
        if salis not in naudoti:
            naudoti.append(salis)
            break
    spetas=str(input(f"Valstybė: {salis}, Miestas: ")).lower()
    spejimai+=1
    if spetas==miestas.lower():
        print("Atspėjai!")
        atspeti+=1
    else:
        print(f"Neatspėjai! Sostinė buvo {miestas}")
    print(f"{atspeti}/{spejimai}")
    if spejimai-atspeti>2:
        print("Žaidimas baigėsi")
        print("")
        break
try:
    if visi_zaidejai[vardas]<atspeti:
        print(f"Rekordą pagerinai")
        visi_zaidejai[vardas]=atspeti
    else:
        print(f"Rekordo ({visi_zaidejai[vardas]}) nepagerinai")
except:
    visi_zaidejai[vardas]=atspeti
    print("Buvai įrašytas į rezultattus (rezultatai.txt faile)")
visi_zaidejai=dict(sorted(visi_zaidejai.items(), key=lambda item: item[1], reverse=True))
#print(visi_zaidejai)
zaidejai=list(visi_zaidejai.keys())
#print(zaidejai)
rezultatai=list(visi_zaidejai.values())
#print(rezultatai)
with open ("rezultatai3.txt", "w") as rf:
    for i in range(len(visi_zaidejai)):
        rf.write(f"{zaidejai[i]} - {rezultatai[i]}\n")
