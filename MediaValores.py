qtd = 0
soma = 0
media = 0
valor = float(input("Informe um valor: "))

while (valor > 0.0):
    soma = soma + valor
    qtd = qtd + 1
    # Entrada de valores
    valor = float(input("Informe um valor: "))

#caso digite um valor negativo o laço encerra
media = soma / qtd
print("\n total da soma: ",soma)
print("\n quantidade de valores digitados: ",qtd)
print("\n media dos valores: ",media)
# Fim do programa