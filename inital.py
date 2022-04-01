bet = int(input('введите ставку'))
C7 = 0
C8 = 0
C9 = 0
C10 = 0
CJ = 0
CQ = 0
CK = 0
CA = 0
Cjackpot = 0
C6 = 0
from random import randint
N = 1
f = [0]*N
b = [0]*N
c = [0]*N
d = [0]*N
e = [0]*N
for i in range (N):
    f[i] = randint(1,1001)
    b[i] = randint(1, 1001)
    c[i] = randint(1, 1001)
    d[i] = randint(1, 1001)
    e[i] = randint(1, 1001)
    f = str(f[i])
    f = int(f)
    b = str(b[i])
    b = int(b)
    c = str(c[i])
    c = int(c)
    d = str(d[i])
    d = int(d)
    e = str(e[i])
    e = int(e)
if 0 < f < 301:
    i1 = '9'
if 300 < f < 451:
    i1 = '10'
if 450 < f < 551:
    i1 = 'j'
if 550 < f < 601:
    i1 = 'Q'
if 600 < f < 626:
    i1 = 'K'
if 625 < f < 636:
    i1 = 'A'
if 635 < f < 641:
    i1 = 'jackpot'
if 640 < f < 741:
    i1 = '6'
if 740 < f < 901:
    i1 = '8'
if 900 < f < 1001:
    i1 = '7'
if 0 < b < 301:
    i2 = '9'
if 300 < b < 451:
    i2 = '10'
if 450 < b < 551:
    i2 = 'j'
if 550 < b < 601:
    i2 = 'Q'
if 600 < b < 626:
    i2 = 'K'
if 625 < b < 636:
    i2 = 'A'
if 635 < b < 641:
    i2 = 'jackpot'
if 640 < b < 741:
    i2 = '6'
if 740 < b < 901:
    i2 = '8'
if 900 < b < 1001:
    i2 = '7'
if 0 < c < 301:
    i3 = '9'
if 300 < c < 451:
    i3 = '10'
if 450 < c < 551:
    i3 = 'j'
if 550 < c < 601:
    i3 = 'Q'
if 600 < c < 626:
    i3 = 'K'
if 625 < c < 636:
    i3 = 'A'
if 635 < c < 641:
    i3 = 'jackpot'
if 640 < c < 741:
    i3 = '6'
if 740< c < 901:
    i3 = '8'
if 900 < c < 1001:
    i3 = '7'
if 0 < d < 301:
    i4 = '9'
if 300 < d < 451:
    i4 = '10'
if 450 < d < 551:
    i4 = 'j'
if 550 < d < 601:
    i4 = 'Q'
if 600 < d < 626:
    i4 = 'K'
if 625 < d < 636:
    i4 = 'A'
if 635 < d < 641:
    i4 = 'jackpot'
if 640 < d < 741:
    i4 = '6'
if 740 < d < 901:
    i4 = '8'
if 900 < d < 1001:
    i4 = '7'
if 0 < e < 301:
    i5 = '9'
if 300 < e < 451:
    i5 = '10'
if 450 < e < 551:
    i5 = 'j'
if 550 < e < 601:
    i5 = 'Q'
if 600 < e < 626:
    i5 = 'K'
if 625 < e < 636:
    i5 = 'A'
if 635 < e < 641:
    i5 = 'jackpot'
if 640 < e < 741:
    i5 = '6'
if 740 < e < 901:
    i5 = '8'
if 900 < e < 1001:
    i5 = '7'
if '6' in i1:
    C6 = C6+1
if '7' in i1:
    C7 = C7+1
if '8' in i1:
    C8 = C8+1
if '9' in i1:
    C9 = C9+1
if '10' in i1:
    C10 = C10+1
if 'j' in i1:
    CJ = CJ+1
if 'Q' in i1:
    CQ = CQ+1
if 'K' in i1:
    CK = CK+1
if 'A' in i1:
    CA = CA+1
if 'jackpot' in i1:
    Cjackpot = Cjackpot+1
if '6' in i2:
    C6 = C6+1
if '7' in i2:
    C7 = C7+1
if '8' in i2:
    C8 = C8+1
if '9' in i2:
    C9 = C9+1
if '10' in i2:
    C10 = C10+1
if 'j' in i2:
    CJ = CJ+1
if 'Q' in i2:
    CQ = CQ+1
if 'K' in i2:
    CK = CK+1
if 'A' in i2:
    CA = CA+1
if 'jackpot' in i2:
    Cjackpot = Cjackpot+1
if '6' in i3:
    C6 = C6+1
if '7' in i3:
    C7 = C7+1
if '8' in i3:
    C8 = C8+1
if '9' in i3:
    C9 = C9+1
if '10' in i3:
    C10 = C10+1
if 'j' in i3:
    CJ = CJ+1
if 'Q' in i3:
    CQ = CQ+1
if 'K' in i3:
    CK = CK+1
if 'A' in i3:
    CA = CA+1
if 'jackpot' in i3:
    Cjackpot = Cjackpot+1
if '6' in i4:
    C6 = C6+1
if '7' in i4:
    C7 = C7+1
if '8' in i4:
    C8 = C8+1
if '9' in i4:
    C9 = C9+1
if '10' in i4:
    C10 = C10+1
if 'j' in i4:
    CJ = CJ+1
if 'Q' in i4:
    CQ = CQ+1
if 'K' in i4:
    CK = CK+1
if 'A' in i4:
    CA = CA+1
if 'jackpot' in i4:
    Cjackpot = Cjackpot+1
if '6' in i5:
    C6 = C6+1
if '7' in i5:
    C7 = C7+1
if '8' in i5:
    C8 = C8+1
if '9' in i5:
    C9 = C9+1
if '10' in i5:
    C10 = C10+1
if 'j' in i5:
    CJ = CJ+1
if 'Q' in i5:
    CQ = CQ+1
if 'K' in i5:
    CK = CK+1
if 'A' in i5:
    CA = CA+1
if 'jackpot' in i5:
    Cjackpot = Cjackpot+1
if C6 == 2:
    bet = 6/10*bet 
if C6 == 3:
    bet = 666/100*bet 
if C7 == 3:
    bet = 77/10*bet 
if C8 == 2:
    bet = 8/10*bet 
if C8 == 3 or C8 == 4:
    bet = 11/10*bet 
if C8 == 5:
    bet = 4*bet 
if C9 == 2:
    bet = 9/10*bet 
if C9 == 3 or C9 == 4:
    bet = 13/10*bet 
if C9 == 5:
    bet = 45/10*bet 
if C10 == 2:
    bet = bet 
if C10 == 3 or C10 == 4:
    bet = 15/10*bet 
if C10 == 5:
    bet = 5*bet 
if CJ == 2:
    bet = 11/10*bet 
if CJ == 3 or CJ == 4:
    bet = 17/10*bet 
if CJ == 5:
    bet = 55/10*bet 
if CQ == 2:
    bet = 12/10*bet 
if CQ == 3 or CQ == 4:
    bet = 19/10*bet 
if CQ == 5:
    bet = 6*bet 
if CK == 2:
    bet = 13/10*bet 
if CK == 3 or CK == 4:
    bet = 21/10*bet 
if CK == 5:
    bet = 8*bet 
if CA == 2:
    bet = 2*bet 
if CA == 3 or CA == 4:
    bet = 8*bet 
if CA == 5:
    bet = 10*bet 
if Cjackpot == 2:
    bet = 10*bet 
if Cjackpot == 3:
    bet = 20*bet 
if Cjackpot == 4:
    bet = 50*bet 
if Cjackpot == 5:
    bet = 100*bet 
if C6>1 or C7>1 or C8>1 or C9>1 or C10>1 or CJ>1 or CQ>1 or CK>1 or CA>1 or Cjackpot>1:
    bet = bet 
else:
    bet = 0
print(i1,i2,i3,i4,i5)
print(bet )
if Cjackpot == 2:
    print('JACKPOT')
if Cjackpot == 3:
    print('SUPER JACKPOT')
if Cjackpot == 4:
    print('MEGA JACKPOT')
if Cjackpot == 5:
    print('HYPER JACKPOT')
