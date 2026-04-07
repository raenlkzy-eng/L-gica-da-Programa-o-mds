nome = input("Poe teu nome rs: ")
idade = int(input("Diga sua idade elemento: "))
dias = idade * 365
meses = idade * 12
partido = input("Qual seu partido? ")
print("Olá", nome, ", prazer.")
print("Uau, você já viveu incrivéis", dias, "dias e", meses, "meses!")
if partido == "esquerda":
    print("Vá estudar!")
elif partido == "direita":
    print("Você é estudado!")
else:
    print("Não entendi seu partido.")