'''
n = int(input())
fact = 1
for i in range(1, n+1):
  fact = fact * i 
#print(fact)

d = [int(d) for d in str(fact)]
counter1 = 0

length = len(d)
#print(d)
#print(length)
for j in reversed(d):
    if(j!=0):
           break
    counter1 += 1
    
print(counter1)

'''

n = int(input())

zero  = 0
while n >= 5:
    zero += n//5
    n = n //5
print(zero)
