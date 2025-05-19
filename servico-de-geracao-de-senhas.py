import random
import string

def gerar_senha(tamanho, letras, numeros, simbolos ):
    if letras == False and numeros == False and simbolos == False:
        print ("Erro ao gerar senha")
        exit()
    caracteres = "" 
    senha = ""
    if letras == True:
        caracteres += string.ascii_letters
    if numeros == True:
        caracteres += string.digits
    if simbolos == True:
        caracteres += string.punctuation
    for i in range(tamanho):
        senha += senha.join(random.choice(caracteres))

    return senha


# Exemplo de uso:
print ("=========Seja bem vindo ao gerador de senhas=========")
tamanho = int(input("informe a quantidade de digitos: "))
letras = True if input ("informe 1 para letras ou 0 para senha sem letras: ") == "1" else False
numeros = True if input ("informe 1 para numeros ou 0 para senha sem numeros: ") == "1" else False
simbolos = True if input ("informe 1 para simbolos ou 0 para senha sem simbolos: ") == "1" else False
senha = gerar_senha(tamanho, letras, numeros, simbolos)
print("Sua senha aleatória é:", senha)