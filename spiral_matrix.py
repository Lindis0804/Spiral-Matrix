def spiralNumbers(n):
    List = [[0 for row in range(0,n)] for col in range(0,n)]
    count =1
    for i in range(n,0,-2):
        l = int((n-i)/2)
        for j in range(l,l+i):
            List[l][j] = count
            count = count+1
        for j in range(l+1,l+i):
            List[j][l+i-1] = count
            count = count+1
        for j in range(l+i-2,l-1,-1):
            List[l+i-1][j] = count
            count = count+1
        for j in range(l+i-2,l,-1):
            List[j][l] = count
            count = count+1
    return List
print(spiralNumbers(int(input())))
        


        

