def toogle(s,i,j,moves):
    if moves%2 != 0:
        for x,y in (0,0),(1,0),(0,-1),(-1,0),(0,1):
            s[i+x][j+y] =  int(not bool(s[i+x][j+y]))  
    return s

s = [[1]*5 for _ in range(5)]

entrada = [list(map(int,input().split())) for _ in (1,2,3)]

for i in range(1,4):
    for j in range(1,4):
        s = toogle(s,i,j,entrada[i-1][j-1])

for i in 1,2,3:
    for j in 1,2,3:
        print(s[i][j],end='')
    print()  