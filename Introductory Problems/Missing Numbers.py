n = int(input())
lst = []
#for i in range(0,n -1):
 #lst = input().spilt(',')
 #   lst.append(ele)
lst = list(map(int,input().split()))
#print(lst)
def missingelement(lst):
    n = len(lst)
    total = (n+1)*(n+2)/2
    sumOflist = sum(lst)
    return int(total) - int(sumOflist)

miss = missingelement(lst)
print(miss)