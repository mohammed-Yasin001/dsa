num = 844
n= num
result = 0
while n > 0:
    last_digit = n % 10
    result = (result * 10) + last_digit
    n //= 10
if num == result:
    print("YES")
else:
    print("NO")
