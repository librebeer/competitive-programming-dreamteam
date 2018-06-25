n = int(input())
data = []
tmp = None
x,y,z = 0,0,0
for i in range(n):
    tmp = list(map(int, input().split(' ')))
    x+=tmp[0]
    y+=tmp[1]
    z+=tmp[2]

print('YES' if (x==0 and y==0 and z==0) else 'NO')