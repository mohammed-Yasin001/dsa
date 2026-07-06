num = 1634
nod = len(str(num))
n = num
result = 0
while n > 0:
    ld = n % 10
    result = ld**nod + result
    n = n // 10

if result == num:
    print("yes")
else:
    print("no")