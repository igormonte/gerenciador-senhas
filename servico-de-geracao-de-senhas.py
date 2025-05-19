import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation

    senha = ""
    for i in range(tamanho-1):
        senha += senha.join(random.choice(caracteres))

    return senha


# Exemplo de uso:
senha = gerar_senha(18)
print("Sua senha aleatória é:", senha)