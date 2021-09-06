N = int(input())
persons = range(1, N + 1)
entrada = list(map(int, input().split()))
posicao = entrada.index(min(entrada))

print(persons[posicao])
