"""
sexo = input("digite seu sexo M/F: ").strip().upper()
while sexo not in ["M", "F"]:
    print("Sexo inválido. Por favor, digite M para masculino ou F para feminino.")
    sexo = input("digite seu sexo M/F: ").strip().upper()
    
print(f"Sexo digitado: {sexo}")
"""
x = int(input("Digite um número de 1 a 10 para ver se voce adinhou meu numero: "))
tentativas = 1
while x != 7:
    print("infelismente errou. Tente novamente.")
    x = int(input("Digite um número de 1 a 10 para ver se voce adinhou meu numero: "))
    tentativas += 1
    if x == 7:
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
    if 1 <= x <= 4 or 9 <= x <= 10:
        print("Dica: Você está frio.")
    if 7 < x <= 8:
        print("Dica: Você está quente.")
print("Voce acertou o número 7!")
