largpalin = 0
for a in range(100,999):
    for b in range(100,999):
        palin = str(a*b)
        l1 =len(palin)/2
        l2 = len(palin)
        palindrome = True
        for x in range(int(l1)):
            if palin[x] != palin[l2-x-1]:
                palindrome = False
                break
        if palindrome:
            if int(palin) > int(largpalin):
                print(palin)
                largpalin = palin
