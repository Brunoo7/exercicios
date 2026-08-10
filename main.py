num = int(input("Insira um número inteiro: "))

if num % 2 == 0:
    print(f"O número {num} é par.")
else:
    print(f"O número {num} é ímpar.")

idade = int(input("Insira sua idade: "))
if 0<= idade <= 12:
    print("Você é uma criança.")

elif 13 <= idade <= 18:
    print("Você é um adolescente.")

else:
    print("Você é um adulto.")