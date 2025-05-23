notaA=float(input("Informe a primeira nota: "))
notaB=float(input("Informe a segunda nota: "))

#Calculo da media
mediafinal = (notaA + notaB) / 2

#verificação da media
if mediafinal >= 7:
    print("A media: %.1f - Aprovado" % mediafinal)
else:
    print("A media: %.1f - Reprovado" % mediafinal)