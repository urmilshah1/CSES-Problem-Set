from itertools import permutations

string = str(input())

x = (''.join(i) for i in list(set(permutations(string))))

sorted_list = sorted(x)

print(len(sorted_list))
for i in sorted_list:
    print(i)
