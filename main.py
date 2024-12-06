programa=0
if programa==0:
    programa=int(input("Įveskite programos numerį -> "))
if programa==1:
    import programa1
    programa1
elif programa==2:
    import programa2
    programa2
elif programa==3:
    import programa3
    programa3
else:
    print(f"Programa {programa} neegzistuoja")
