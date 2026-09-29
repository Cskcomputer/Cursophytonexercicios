sexo = input("digite seu sexo M/F: ").strip().upper()
while sexo not in ["M", "F"]:
    print("Sexo inválido. Por favor, digite M para masculino ou F para feminino.")
    sexo = input("digite seu sexo M/F: ").strip().upper()
    
print(f"Sexo digitado: {sexo}")
