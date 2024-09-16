import math
class Operacao:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def coletar(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def somar(self, num1, num2):
        self.coletar(num1, num2) #Utilizando o método coletar
        return self.num1 + self.num2

    def subtrair(self, num1, num2):
        self.coletar(num1, num2)
        return self.num1 - self.num2

    def multiplicar(self, num1, num2):
        self.coletar(num1, num2)
        return self.num1 * self.num2

    def dividir(self,num1, num2):
        self.coletar(num1, num2)
        if self.num2 <= 0:
            return "Impossível divir!"
        else:
            return self.num1 / self.num2

    def tabuada(self, num1):
        resultado = ""
        for i in range(0,11,1):
            resultado += f'\n{num1} * {i} = {num1 * i}'
        return resultado

    def potencia(self, base, expoente):
        return pow(base, expoente)

    def raiz(self, num):
        return math.sqrt(num)

    def imprimir(self):
        result = ""
        for i in range(0,11,1):
            result += f'\n{i}'
        return result

    def imprimirpa(self):
        pares = ""
        for i in range(0, 21, 1):
           if i % 2 == 0:
               pares += f'\n{i}'
        return pares

    def cemnum(self):
        soma = 0
        for i in range(1, 101):
            soma += i
        return soma

    def divisores(self):
        divi = ""
        for i in range (1, 51,1):
            if i % 5 == 0:
                divi += f'\n{i}'
        return divi
    def imppar(self, num1):
        if num1 % 2 == 0:
            return 'Número par!'
        else:
            return "Número ímpar"
    def desc(self, num1):
        if num1 < 0:
            return "Número negativo!"
        if num1 == 0:
            return "Número zero!"
        else:
            return "Número positivo!"
    def numusu(self, num1):
        result = ""
        for i in range(0, 11, 1):
            result += f'\n{num1} * {i} = {num1 * i}'
        return result
    def imprimirate(self, num1):
        result = ""
        for i in range (0, num1 + 1, 1 ):
            result += f'\n{i}'
        return result

    def somarate(self, num1):
        result = 0
        for i in range (0, num1 + 1, 1 ):
            result += i
        return result

    def fatorial(self, num1):
        soma = 1
        for i in range(1,num1,1):
            soma += soma * i
        return soma

    def primos(self):
        primo = "1\n2\n3\n4"
        for i in range(5,21,1):
            if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
                primo += f'\n{i}'
        return primo

    def ehPrimo(self, num1):
        if num1 == 2 or num1 == 3 or num1 == 5:
            return f'0 {num1} é primo!'
        elif num1 % 2 != 0 and num1 % 3 != 0 and num1 % 5 !=0:
            return f'0 {num1} é primo!'
        return f'O {num1} não é primo!'

    def collatz(self,num1):
        resultado = ""
        for i in range(1, num1):
            if i % 2 == 0:
                resultado += f'\n{i / 2}'
            else:
                resultado += f'\n{i * 3 + 1}'
        return resultado

    def fibonnaci(self):
        n = int(input(" Digite Quantos termos você deseja :"))
        num1 = 0
        num2 = 1
        num3 = 0

        while num3 <= n:
            print("{}.".format(num3), end="")
            num3 = num1 + num2
            num1 = num2
            num2 = num3

    def somUsu(self, num1):
        soma = 0
        a = num1
        b = str(a)
        for i in range(len(b)):
            soma += int(b[i])
        return soma

    def listPeI(self,num1):
        resultado = ""
        for i in range(1, num1):
            if i % 2 == 0:
                resultado += f'\n{i} Par'
            else:
                resultado += f'\n{i} Impar'
        return resultado
    def imprimirPrimos(self,num1):
        primo = ""
        for i in range(1,num1,1):
            if i == 2 or i == 3 or i == 5:
                primo += f'\n{i}'
            elif num1 % 2 != 0 and num1 % 3 != 0 and num1 % 5 != 0:
                primo += f'\n{i}'
        return primo

    def somIeP(self,num1):
        par = 0
        impar = 0
        for i in range(1,num1 + 1):
            if i % 2 == 0:
                par += i
            else:
                impar += i
        return f'A soma dos pares é de:{par}, e dos ímpares é:{impar}'
    def ex1list2(self, num1 , num2):
        num1 = num2
        num2 = num1
        return {num1} , {num2}

    def ex2list2(self,num1):
        return num1 - 1

    def ex3list2(self, num1 , num2):
        resultado = num1 * num2
        return resultado
    def ex4list2(self,num1):
        num1 = 365 * num1
        return num1




















