print("----------------Programa 2----------------")
suvestine={}
with open ("duomenys2.txt", "r") as df:
    ilgis=len(df.readlines())
with open ("duomenys2.txt", "r") as df:
    for i in range(ilgis):
        line=list(map(str, df.readline().strip().split()))
        vardas=line[0]
        line.remove(line[0])
        suvestine[vardas]=sum(map(int, line))
    suvestine=dict(sorted(suvestine.items(), key=lambda item: item[1], reverse=True))
    with open ("rezultatai2.txt", "w") as rf:
        for vardas1, suma in suvestine.items():
            rf.write(f"{vardas1} {suma}\n")
print("Rezultatai įrašyti į rezultatai2.txt")
