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

sarakts1 = [1, 7, 5, 9, 35, 2]
sarakts2 = [4, 2, 2, 39, 6, 4]
for skatitajs in range (len(sarakts1)):
    print("pirmais skaitlis:", sarakts1[skatitajs], "otrais skaitlis:", sarakts2[skatitajs], "rezultats", rezultats(sarakts1[skatitajs], sarakts2[skatitajs]))

    skaitlu_pari = [[2,5], [4,7], [3,4], [7,9]]
    for i in range(len(skaitlu_pari))

print("--------------")

i = 1
for in range(len(skaitlu_pari))