#Exercício 01

altura = float(input("Digite a altura pirâmide"))
base_menor = float(input("Digite a base menor da pirâmide"))
base_maior = float(input("Digite a base menor da pirâmide"))
volume = altura/3*(base_maior**2 + base_menor**2 + (base_maior**2*base_menor**2)**0.5)

print ("O Volume do tornco da pirâmide é: ", volume)

#Exercício 2 

qnt_horas = int(input("Digite um valor em horas: "))
valor_minutos = (qnt_horas * 60)
print ("O valor em minutos é: ", valor_minutos)

#Exercício 3

anos = int(input("Digíte sua idade em anos: "))
meses = int(anos*12)
dias = (anos*365)

print ("Você tem: ", anos,"Anos")
print ("Sua idade em meses é: ", meses,"Meses")
print ("Sua idade em dias é: ", dias,"Dias")