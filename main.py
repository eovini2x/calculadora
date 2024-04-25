#funcao de adicao 
def add(x, y):
  return x + y 
  
#funca de subtracao 
def sub (x, y):
  return x - y 
  
#duncao multiplicacao
def mult (x, y):
  return x * y 
  
#funcao dedivisao
def div(x, y):
  return x / y

#calculadora 
print("selecione uma operacao .")
print("1. Adicao")
print("2. Subtracao")
print("3. Multiplicacao")
print("4. Divisao")

while True:
  escolha = input("Escolha um numero (1/2/3/4): ")

  if escolha in ('1', '2', '3', '4',):
    num1 = float(input("digite um numero: "))
    num2 = float(input("digite outro numero: "))
    if escolha == '1':
      print(num1, "+", num2, "=", add(num1, num2))

    elif escolha == '2':
      print(num1, "-", num2, "=", sub(num1, num2))

    elif escolha == '3':
     print(num1, "*", num2, "=", mult(num1, num2))

    elif escolha == '4':
     print(num1,"/", num2, "=", div(num1, num2))

    else:
       print("numero invalido.")