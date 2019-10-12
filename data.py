import csv
import math

def getValues():
    with open("data.txt") as f:
        reader = csv.reader(f, delimiter="\t")
        d = list(reader)
    return d

#print(getValues())

def PLauf(a, b, M, c):
    if M < b:
        P = math.floor(a * (b - M) ** c)
    else:
        P = 0
    return P

def PWuSp(a, b, M, c):
    if M > b:
        P = math.floor(a * (M - b) ** c)
    else:
        P = 0
    return P

def P100M(M):
    d = getValues()
    a = float(d[3][1])
    b = float(d[3][2])
    c = float(d[3][3])
    return PLauf(a, b, M, c)

def PWeit(M):
    d = getValues()
    a = float(d[12][1])
    b = float(d[12][2])
    c = float(d[12][3])
    return PWuSp(a, b, M, c)

def PKugel(M):
    d = getValues()
    a = float(d[15][1])
    b = float(d[15][2])
    c = float(d[15][3])
    return PWuSp(a, b, M, c)

def PHoch(M):
    d = getValues()
    a = float(d[13][1])
    b = float(d[13][2])
    c = float(d[13][3])
    return PWuSp(a, b, M, c)

def P400M(M):
    d = getValues()
    a = float(d[5][1])
    b = float(d[5][2])
    c = float(d[5][3])
    return PLauf(a, b, M, c)

def P110H(M):
    d = getValues()
    a = float(d[11][1])
    b = float(d[11][2])
    c = float(d[11][3])
    return PLauf(a, b, M, c)

def PDiskus(M):
    d = getValues()
    a = float(d[16][1])
    b = float(d[16][2])
    c = float(d[16][3])
    return PWuSp(a, b, M, c)

def PStab(M):
    d = getValues()
    a = float(d[14][1])
    b = float(d[14][2])
    c = float(d[14][3])
    return PWuSp(a, b, M, c)

def PSpeer(M):
    d = getValues()
    a = float(d[17][1])
    b = float(d[17][2])
    c = float(d[17][3])
    return PWuSp(a, b, M, c)

def P1500(M):
    d = getValues()
    a = float(d[8][1])
    b = float(d[8][2])
    c = float(d[8][3])
    return PWuSp(a, b, M, c)

# print(PLauf(25.4347,18, 10.21, 1.81))
# print(PWeit(781),PStab(500), P1500(4.1), P110H(14.02))
