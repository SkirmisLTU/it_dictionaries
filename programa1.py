print("----------------Programa 1----------------")
kiekis=int(input("Kiek žmonių norėsite įvesti? -> "))
zmones={}
for i in range (kiekis):
    print(f"----------{i+1}----------")
    vardas=str(input("Įveskite vardą -> "))
    amzius=int(input("Įveskite amžiu -> "))
    zmones[vardas]=amzius
for vardas, amzius in zmones.items():
    print(f"Vardas: {vardas}, Amžius: {amzius}")
for vardas, amzius in zmones.items():
    print(vardas, end=" ")
print("")
for vardas, amzius in zmones.items():
    print(amzius, end=" ")
print("")
print(f"Du vyriausi: ",end="")
zmones_temp = zmones.copy()
for i in range(2):
    did=max(zmones_temp, key=zmones_temp.get)
    print(did,end=" ")
    zmones_temp[did]=0
print("")
visu_amzius=[]
for vardas, amzius in zmones.items():
    visu_amzius.append(int(amzius))
    print(amzius)
print(visu_amzius)
print(f"Vidutinis amžius: {round(sum(visu_amzius)/len(visu_amzius),1)}")
