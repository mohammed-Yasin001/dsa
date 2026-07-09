n = [5,3,2,3,4,5,3,5,4,44,4,8,9,10]
m = [10,11,1,9,5,3,2]

max_val = max(n)
hash_list = [0] * (max_val + 1)

for num in n:
    hash_list[num] += 1

for num in m:
    print(f"{num}:{hash_list[num]}")


