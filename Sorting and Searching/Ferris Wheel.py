n, x  = input().split()
weight_of_child = []
weight_of_child =  list(map(int, input().split()))

for i in weight_of_child:
    if sum(i, i+1) < x:
        gon.append(i, i+1)
    print(gon)
   


print(weight_of_child)