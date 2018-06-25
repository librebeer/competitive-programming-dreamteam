n = int(input())
s = input()
c= s[0]
counter = 0
for i in range(1,n):
    if s[i] == c:
        pass
        counter+=1
    else:
        c = s[i]
print(counter)