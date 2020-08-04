t = int(input())
b = [[int(i) for i in input().split()] for j in range(t)]
    
for i in range(t):
    f1, f2 = b[i][0], b[i][1]
    if f1 <= f2*2 and f2 <= f1 *2 and (f1+f2)%3==0:
        print("YES")
    else:
        print("NO")