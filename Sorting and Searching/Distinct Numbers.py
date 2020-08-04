'''def unique(nums):
    unique_list = {}
    
    for x in nums:
        unique_list.add(x)
    
    
    count = len(unique_list)
    print(count)
  '''  

    

n = int(input())
nums = list(map(int,input().split()))
unique_list = set(nums)
print(len(unique_list))
#unique(nums)