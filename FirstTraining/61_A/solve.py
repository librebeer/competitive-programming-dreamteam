from sys import stdin
a = stdin.readline()
b = stdin.readline()
r =''
for i in range(len(a)-1):
    r+=str(int(bool(int(a[i])) != bool(int(b[i]))))
print(r)


