#crie uma função que calcule a área do retângulo

def area(base,altura):
   resultado = base * altura
   print(f"Área do retângulo: {resultado}")

base = int(input("Digite a base do retângulo: "))
altura = int(input("Digite a altura do retângulo: "))

#chamo a função: para fazer a função funcionar, precisa "chamar ela" ou repetir a forma que foi escrito a função e na indentação.

area(base,altura)