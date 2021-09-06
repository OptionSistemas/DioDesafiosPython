a, b, c, d = input().split(" ")

hora_inicial = int(a)
minuto_inicial = int(b)
hora_final = int(c)
minuto_final = int(d)

if (hora_inicial > hora_final):
    hora = int((24 - hora_inicial) + hora_final)
elif (hora_inicial < hora_final):
    hora = int(hora_final - hora_inicial)
else:
    if (minuto_final <= minuto_inicial):
        hora = int(24)
    else:
        hora = int(0)

if (minuto_final > minuto_inicial):
    minuto = int(minuto_final - minuto_inicial)
elif (minuto_final < minuto_inicial):
    minuto = int((60 - minuto_inicial) + minuto_final)
    hora = hora - 1
else:
    minuto = int(0)

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hora, minuto))
