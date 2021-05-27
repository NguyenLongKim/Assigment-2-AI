
a = [[1,2,3],
    [1,2,3]]
a= [(i,j) for i in range(3) for j in range(3) if (i+j)%2==0]

print(a)