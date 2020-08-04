n =  int(input())
lis = list(map(int, input().split()))
print(lis)
lis.sort()

a = len(lis)


first_list = lis[0: a//2]   
second_list = lis[a//2:a]


print(first_list)
print(second_list)

