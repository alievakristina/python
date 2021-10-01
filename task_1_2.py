a = []
for i in range(1000):
    if i % 2 != 0:
        a.append(i ** 3)
print(a)

b = []
sum1 = 0
for num in a:
    i = num
    while num != 0:
        sum1 += num % 10
        num = num // 10
    if sum1 % 7 == 0:
        b.append(i)
    sum1 = 0
print(sum(b))

sum_num_plus = 0
for num in a:
    summ = 0
    i = num
    num += 17
    while num != 0:
        summ += num % 10
        num = num // 10
    if summ % 7 == 0:
        sum_num_plus += i
print(sum_num_plus)