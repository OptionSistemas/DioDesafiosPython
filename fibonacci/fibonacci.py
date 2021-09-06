def fib(numero):
    a, b = 0, 1
    fib_list = []
    while len(fib_list) < numero:
        fib_list.append(str(a))
        a, b = b, a+b

    print(' '.join(fib_list))


n = int(input())
fib(n)


