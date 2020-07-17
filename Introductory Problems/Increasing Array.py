n = int(input())
lst = []
count = 0

lst = list(map(int,input().split()))
#print(lst)

for i in range(1, n):
     if lst[i] < lst[i-1]:
      count = count + (lst[i-1] - lst[i])
      lst[i] = lst[i-1]
print(count)
