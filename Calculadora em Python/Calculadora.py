print("\n")
print("Calculadora em Pyhton!")

i = int(0)
n1 = float(input("Digite um numero: "))

while i == 0:
    calculo = input("Que calculo deseja fazer? soma = +, subtração = -, multiplicação = *, divisão = /:, potenciação = ^: ")
    if calculo == "+" or calculo == "-" or calculo == "*" or calculo == "/" or calculo == "^": i+=1
    
    else: calculo = input("Que calculo deseja fazer? soma = +, subtração = -, multiplicação = *, divisão = /:, potenciação = ^: ")

n2 = float(input("Digite outro numero: "))

if calculo == "+":
 
    print("O resultado da soma de " + str(n1) + " + " + str(n2)+ " é: " + str(n1+n2))
 
elif calculo == "-":
    print("O resultado da subtração de " + str(n1) + " - " + str(n2)+ " é: " + str(n1-n2))

elif calculo == "*":
    print("O resultado da multiplicação de " + str(n1) + " * " + str(n2)+ " é: " + str(n1*n2))

elif calculo == "^":
    print("O resultado da potenciação de " + str(n1) + " ^ " + str(n2)+ " é: " + str(n1**n2))
    
elif calculo == "/":
    
    if n2 == 0:
        print("Não é possivel dividir por 0!")

    else: print("O resultado da divisão de " + str(n1) + " / " + str(n2)+ " é: " + str(n1/n2))
else: print("Alguma coisa deu errado!")