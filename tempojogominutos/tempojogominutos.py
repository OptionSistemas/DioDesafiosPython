from datetime import datetime, timedelta

horaInicial, minutoInicial, horaFinal, minutoFinal = input().split()
diasDeltaInicio = 1 if horaInicial == '24' else 0
diasDeltaTermino = 1 if horaFinal == '24' else 0
horaInicial = "00" if horaInicial == '24' else horaInicial
horaFinal = "00" if horaFinal == '24' else horaFinal


horaDeltaInicio = 1 if minutoInicial == '60' else 0
horaDeltaTermino = 1 if minutoFinal == '60' else 0
minutoInicial = "00" if minutoInicial == '60' else minutoInicial
minutoFinal = "00" if minutoFinal == '60' else minutoFinal

horaInicial = horaInicial if int(horaInicial) >= 0 else str(abs(int(horaInicial)))
horaFinal = horaFinal if int(horaFinal) >= 0 else str(abs(int(horaFinal)))

minutoInicial = minutoInicial if int(minutoInicial) >= 0 else str(abs(int(minutoInicial)))
minutoFinal = minutoFinal if int(minutoFinal) >= 0 else str(abs(int(minutoFinal)))

horaTermino = datetime.strptime(f"{horaFinal.zfill(2)}:{minutoFinal.zfill(2)}", "%H:%M") + timedelta(
    days=diasDeltaTermino, hours=horaDeltaTermino)
horaInicio = datetime.strptime(f"{horaInicial.zfill(2)}:{minutoInicial.zfill(2)}", "%H:%M") + timedelta(
    days=diasDeltaInicio, hours=horaDeltaInicio)

# print(horaInicio)
# print(horaTermino)
if (horaInicio == horaTermino) or (horaInicio > horaTermino):
    horaTermino += timedelta(days=1)
difHoras = horaTermino - horaInicio

horas, resto = divmod(difHoras.seconds, 3600)
minutos, segundos = divmod(resto, 60)
if difHoras.days > 0:
    # horas, minutos = 24, 0
    horas = 24
print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
