n = int(input())
fib_list = []
a, b = 0, 1
for i in range(n):
    fib_list.append(str(a))
    a, b = b, a + b

fib_string = ' '.join(fib_list)
print(fib_string)
