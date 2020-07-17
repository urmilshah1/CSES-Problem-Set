n =  int(input())
ls = []
ls = list(range(1,n+1))
ls1 = []
ls2 = []
lsnew = []
#print(ls)


for i in range(1,n+1):
    if (i%2==0):
       ls1.append(i)
    elif(n==2):
       print("NO SOLUTION")
       break
    elif(n==3):
        print("NO SOLUTION")
        break
    else:
       ls2.append(i)
       
#print(ls1)
#print(ls2)


lsnew = ls1 + ls2
print(lsnew, sep = " ")
