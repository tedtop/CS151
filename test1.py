from my_functions import is_even

# for j in range(0,10):
#     j += j
#     print(j)

# n = 12345
# m = 0
# while n != 0:
#     m = (10 * m) + (n % 10)
#     n = n // 10
#     print(m,n)

count = 0
for i in range(1000, 2000):
    if is_even(i):
        print(i, end=' ')
        count += 1
        if count % 5 == 0:
            print()