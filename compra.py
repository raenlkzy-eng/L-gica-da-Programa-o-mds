nome = input("Nome do cliente: ")
valor = float(input("Valor da compra: "))
pagamento = input("Forma de pagamento: ")#Pix, Crédito, Débito
vip = input("Cliente VIP? ") #Sim ou Não

desconto = 0

#MEIOS DE PAGAMENTO
if pagamento == "Pix":
    desconto += 10
elif pagamento == "Débito":
    desconto += 5
elif pagamento == "Crédito":
    desconto += 0 
    
#CLIENTE VIP
if vip == "Sim" and valor > 300:
    desconto += 5

#VALOR FINAISIEUJ
valor_final = valor - (valor * desconto / 100)

print("\n--- RESUMO DA COMPRA ---")
print(f"Cliente: {nome}")
print(f"Desconto no valor de: {desconto}%")
print(f"Valor total: R$ {valor_final:.2f}")

#CLIENTE ESPECIAL 
if valor_final > 500:
    print("Você é um cliente especial! Agradecemos a preferência!")