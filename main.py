#1-misol
matritsa = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
print(matritsa[0][2])
print(matritsa[2][0])
print(matritsa[1][1])


#2-misol
r = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
natija = []
for qator in r:
    natija.append(qator[0])
print(natija)


#3-misol
son = 5

def oshir():
    son = son + 1
    print(son)


oshir()


#4-misol
son = 5

def oshir():
    global son
    son = son + 1
    print(son)

oshir()
print(son)
