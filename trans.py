matrix=[]
row=int(input('Enter No. of rows'))
col=int(input('Enter No. of Columns'))
for r in range(col):
    t=[]
    for i in range(col):
        elements=int(input('Enter Element'))
        t.append(elements)
    matrix.append(t)
trans=[]
for r in range(row):
    t=[]
    for i in range(col):
        t.append(matrix[i][r])
    trans.append(t)
print('The Transpose is')
for l in range(row):
    print(trans[l])
    
    
