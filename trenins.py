def rezultats(sk1, sk2):
    if sk1<6 and sk2<6:
        rez = sk1+sk2
    else:
        rez = sk1+sk2

    return rez

for skaitlis in range(1,11,2):     #range- funkcija, kas
    print("mūsu skaitlis:", skaitlis, "rezultāts:", rezultats(4, skaitlis))

def zvaigznites (skaits):
    for rindasnr in range(1, skaits+1):
        for zvaigzne in range ( rindasnr):
            print("*", end="")
        print("")

def zvaigznites2(skaits):
    for rindasnr in range(1, skaits+1):
        print("*"*rindasnr)

zvaigznites(7)

skaitlis1 = 4
skaitlis2 = 3

print("pirmais skaitlis:", skaitlis1) 
print("otrais skaitlis:", skaitlis2)
print("summa:", rezultats(skaitlis1, skaitlis2))

