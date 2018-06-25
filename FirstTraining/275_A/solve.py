#Solve Lights Out
#http://codeforces.com/submissions/lehenrry
def toggleLigths(state,i,j,times):
    if times % 2 == 0:
        return state
    else:
        if((i==2) and (j==2)):
            for n in range(3):
                for m in range(3):
                    state[n][m] = not state[n][m]
        else:
            state[i][j] = not state[i][j]
            if i > 0:
                state[i-1][j] = not state[i][j] 
            if i < 2:
                state[i+1][j] = not state[i+1][j]
            if j > 0:
                state[i][j-1] = not state[i][j-1]
            if j < 2:
                state[i][j+1] = not state[i][j+1]
            if i > 0 and j> 0:
                state[i-1][j-1] = not state[i-1][j-1]
            if i < 0 and j< 2:
                state[i+1][j+1] = not state[i+1][j+1]
            if i < 2 and j< 2:
                state[i+1][j+1] = not state[i+1][j+1]
            if i < 2 and j >0:
                state[i+1][j-1] = not state[i+1][j-1]
                
    print('\n'.join(['\t'.join([ str(cell) for cell in row ]) for row in state]))
    
lightState = [[True,True,True] for i in range(3)]
datain = [ list(map(int,input().split(' '))) for i in range(3)]

def solve():
    for i in range(3):
        for k in range(3):
                toggleLigths(lightState,i,k,datain[i][k])
                print(toggleLigths)
                print('----')
#Initial 
#solve()
#print(datain)
print(lightState)
#toggleLigths(lightState,2,2,3)
#toggleLigths(lightState,0,0,3)
#toggleLigths(lightState,0,1,3)
#toggleLigths(lightState,0,2,3)
toggleLigths(lightState,2,0,3)
#toggleLigths(lightState,1,1,3)
