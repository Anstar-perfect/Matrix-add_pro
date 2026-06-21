x = [[3,5,7],[1,7,3]]
y = [[2,5,6],[3,6,0]]
answer = [[0,0,0],[0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        answer[i][j] = x[i][j] - y[i][j]        

for r in answer:
    print(r)        