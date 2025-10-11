# calc.py

def soma(a, b):
    return a + b

def subtração(a, b):
    return a - b

def multiplicação(a, b):
    return a * b

def divisão(a, b):
    if b == 0:
        return None
    return a / b

if __name__ == "__main__":
    num1 = 10
    num2 = 5
    print(f"Soma de {num1} + {num2} = {soma(num1, num2)}")
    print(f"Subtração de {num1} - {num2} = {subtração(num1, num2)}")
    print(f"Multiplicação de {num1} * {num2} = {multiplicação (num1, num2)}")
    print(f"Divisão de {num1} / {num2} = {divisão(num1, num2)}")
    print(f"Divisão de {num1} / 0 = {divisão(num1, 0)}")