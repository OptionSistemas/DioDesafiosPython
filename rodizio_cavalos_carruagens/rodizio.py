import re

n = int(input())
for i in range(1, n + 1):
    dias = ["SEGUNDA", "TERCA", "QUARTA", "QUINTA", "SEXTA"]
    final = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 0)]
    regex = r"^[A-Z]{3}-[0-9]{4}$"
    placa = input()
    if not re.match(regex, placa):
        print('FALHA')
    else:
        finalplaca = int(placa[7])
        for k in range(6):
            if finalplaca in final[k]:
                print(dias[k])
                break
