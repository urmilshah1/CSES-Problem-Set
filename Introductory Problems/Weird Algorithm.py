
def main():
 n =  input()
 n = int(n)
 while(n>1):
    for i in range(n): 
     print(n, end= ' ')
     break
    if (n%2==0):
     n = int(n/2) 
    else:
     n = (n*3) + 1
 print(n)


if __name__== '__main__': main()