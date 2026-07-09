n = [1,2,3,4,3,4,3,5,4,5,3,2,9,8,7,8,8]
m = [10,111,1,12,2,24,34,3,4]

for num in m:
    count = 0
    for x in n:
        if num == x:
            count += 1
    print(f'{num}:{count}')