n = int(input())

lis = []

for i in range(1, n+1):
    lis.append(i)
#print(lis)

for i in lis:
 if(n%2==0):
    print("NO")
    break
 else:
    length = len(lis)
    middle_index = length//2
    one_half = lis[:middle_index]
    second_half = lis[middle_index :]
    if sum(one_half) == sum(second_half):
        print(*one_half, sep= ' ')
        print(*second_half, sep = ' ')
    else:
        print('NO')
        break

