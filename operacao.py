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
        num1 = 10
        num2 = 20
        return {num1 + 10} , {num2 - 10}

    def ex2list2(self,num1):
        return num1 - 1

    def ex3list2(self, num1 , num2):
        resultado = num1 * num2
        return resultado
    def ex4list2(self,num3, num4):
        num3 = num3 * 365
        num4 = num4 * 30
        result = num3 + num4
        return result
    def ex5list2(self,num5,num6,num7,num8):
        num6 = num5 / num6
        num7 = num5 / num7
        num8 = num5 / num8
        return f'A porcentagem de votos brancos é de: {num6}%, a porcentagem de votos nulos é de: {num7}%, a porcentagem de votos válidos é de:{num8}%.'
    def ex6list2(self, num9):
        cont = num9 / 30
        num9 = num9 + cont
        return f'Seu salario com o reajuste é de:{num9}'
    def ex7list2(self,num10):
        imp = num10 / 45
        dis = num10 / 28
        num10 = num10 + imp + dis
        return f'o valor total somando os impostos e a taxa do distribuidor é de: {num10}$'
    def ex8list2(self,num11,num12,num13):
        somaTotal = num11 + num12 + num13 / 3
        return f'A média das notas é de: {somaTotal}'
    def ex9list2(self,num1):
        if num1 < 12:
            num1 * 1.30
        else:
            num1 * 1
        return f'O valor total da compra é de: {num1}$'
    def ex10list2(self, num1):
        maior = ""
        for i in range(1, 11, 1):
            num1 = int(input("Informe um número: "))
            if i == 1:
                maior = num1

            if num1 > maior:
                maior = num1


        return f'O maior número é: {maior}'
    def ex11list2(self, num25, num26):
        if num26 <= 1500:
            conta = num26 / 3
            num25 = num25 + num26 + conta
        else:
            conta = num26 / 8
            num25 = num25 + num26 + conta
        return f'O valor total é de {num25}'
    def ex12list2(self,numero,saldo,debito,credito):
        saldoAtual = saldo - debito + credito
        if saldoAtual > 0:
            return f'O seu saldo de {saldoAtual}$ é positivo!'
        else:
            return f'O seu saldo de {saldoAtual}$ é negativo!'
    def ex13list2(self,num1):
        resultado = ""
        for i in range(1, 11, 1):
            if num1 <= 10:
                resultado += f'\n{num1} * {i} = {num1 * i}'
        return resultado
    def ex14list2(self, num1):
        resultado = ""
        for i in range(0,num1,1):
            resultado += f'\n{i}'
        return resultado
    def ex15list2(self, num1):
        negativos = 0
        for i in range(1, 11, 1):
            num1 = int(input("Informe um número: "))
            if num1 < 0:
                negativos += 1
        return f'A quantidade de negativos é: {negativos}'
    def ex16list2(self, num1):
        soma = -1
        for i in range(11):
            num1 = int(input("Informe um número: "))

            if num1 < 40:
                soma += num1
        return f'A soma dos números menores que 40 é de: {soma}'
    def ex17list2(self,num1):
        total = 0
        for i in range(15, 101, 1):
            num1 = int(input("Informe um número: "))
            total += num1
            media = total / 100
        return f'A média dos números fornecidos é de: {media}'
    def ex18list2(self,num1):
        cont = ""
        total = 0
        maior = ""
        num1 = int(input("Informe um valor: "))
        for i in range(1, num1 + 1, 1):
            cont += f'{i}'
            if i == 1:
                maior = num1

            if num1 > maior:
                maior = num1


            total += num1
            media = total/num1
        return f'De 1 até o maior número digitado: {cont}, O maior número: {maior}, e a média {media} ' #não consegui fazer com que a média pegasse o num1 para dividir pela soma
    def ex19list2(self,num1):
        meed = 0
        total = 0
        for i in range(1, 21, 1):
            num1 = int(input("Informe um número: "))
            total += num1
            media = total / 20
            if num1 > media:
                meed += 1

        return f'A média  é de: {media}, total de alunos acima de média: {meed}' #não consegui terminar





