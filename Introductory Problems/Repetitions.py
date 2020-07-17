str1 = str(input())
length =  len(str1)
counter1 = 0


repeater = str1[0]
for i in range(length):
    count1= 1
    for j in range(i + 1, length):
        
        if (str1[i]!= str1[j]):
            break
        count1 = count1 + 1
         
    if count1 > counter1:
        counter1 = count1
        repeater = str1[i]
    
        
print(counter1)
    