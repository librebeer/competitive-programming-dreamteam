#https://wiki.python.org/moin/BitwiseOperators
a = input()
sa = len(a)
b =input()
sb = len(b)
print(bin((int(a,2)^int(b,2)))[2:].zfill(sa))