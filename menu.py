from operacao import Operacao

class Menu:
    def __init__(self):
        self.opcao = -1
        self.exer = Operacao()
        self.num1 = 0
        self.num2 = 0

    def mostrarMenu(self):
        print("\n ---MENU---\n\n"    +
              "Escolha uma das opções abaixo:"              +
              "\n0. Sair"                                   +
              "\n1.Somar"                                   +
              "\n2.Subtrair"                                +
              "\n3.Dividir"                                 +
              "\n4.Multiplicar"                             +
              "\n5.Potência"                                +
              "\n6.Raiz"                                    +
              "\n7.Tabuada"                                 +
              "\n8. Imprimir"                               +
              "\n9.Imprimir pares"                          +
              "\n10. Imprimir soma dos números de 1 até 100"+
              "\n11. Imprimir divisores de 5 de 1 até 50"   +
              "\n12. Descubra se seu número é ímpar ou par" +
              '\n13. Positivo, negativo ou zero'            +
              "\n14. Informe um número para a taubuada"     +
              "\n15. Informar números até um certo núemro"  +
              "\n16. Soma de n número até o número fornecido" +
              "\n17. Número fatorial"                       +
              "\n18. Números primos"                        +
              "\n19. Números primos pt2"                    +
              "\n20. Sequência de Collatz"                  +
              "\n21. Sequência de Fibonnaci"                +
              "\n22. Soma de números separados"             +
              "\n23. Lista de Pares e Impares"              +
              "\n24. Imprimir Primos"                       +
              "\n25. Soma de Pares e ímpares"               +
              "\n26. A e B"                                 +
              "\n27. Mostrar Antecessor"                    +
              "\n28. Base E Altura"                         +
              "\n29. Idade em dias"                         +
              "\n30. Votos do Município"                    +
              "\n31. Reajuste Salarial"                     +
              "\n32. Custo do carro"                        +
              "\n33. Média do Aluno"                        +
              "\n34. Venda de Maças"                        +
              "\n35. Mostrar maior número"                  +
              "\n36. Salário Fixo"                          +
              "\n37. Saldo"                                 +
              "\n38. Tabuada pt2"                           +
              "\n39. Mostrar Números"                       +
              "\n40. Mostrar Negativos"                     +
              "\n41. Números menores que 40"                +
              "\n42. Média do 15 a 100"                     +
              "\n43. Maior, media, e exibição"              +
              "\n44. Média de 20"

              )

    def coletar(self):
        self.num1 = int(input('Informe o primeiro número:'))
        self.num2 = int(input('Informe o segundo número:'))


    def coletar2(self):
        self.num3 = int(input('Informe sua idade em anos:'))
        self.num4 = int(input('Informe sua idade em meses:'))

    def coletar3(self):
        self.num5 = int(input('Informe o número total de eleitores:'))
        self.num6 = int(input('Informe o número total de votos brancos:'))
        self.num7 = int(input('Informe o número total de votos nulos:'))
        self.num8 = int(input('Informe o número total de votos válidos:'))

    def coletar3(self):
        self.num9 = int(input('Informe o salário atual:'))
    def coletar4(self):
        self.num10 = int(input('Informe o custo do carro:'))
    def coletar5(self):
        self.num11 = int(input('Informe a primeira nota:'))
        self.num12 = int(input('Informe a segunda nota:'))
        self.num13 = int(input('Informe a terceira nota:'))
    def coletar6(self):
        self.num14 = int(input('Informe um número:'))
        self.num15 = int(input('Informe um número:'))
        self.num16 = int(input('Informe um número:'))
        self.num17 = int(input('Informe um número:'))
        self.num18 = int(input('Informe um número:'))
        self.num19 = int(input('Informe um número:'))
        self.num20 = int(input('Informe um número:'))
        self.num21 = int(input('Informe um número:'))
        self.num22 = int(input('Informe um número:'))
        self.num23 = int(input('Informe um número:'))
        self.num24 = int(input('Informe um número:'))
    def coletar7(self):
        self.num25 = int(input('Informe o salário fixo:'))
        self.num26 = int(input('Informe o valor das vendas:'))
    def coletar8(self):
        self.numero = int(input('Informe o número da conta:'))
        self.saldo = int(input('Informe o saldo:'))
        self.debito = int(input('Informe o débito da conta:'))
        self.credito = int(input('Informe o crédito:'))




    def operacao(self):
        while self.opcao != 0:
            self.mostrarMenu()
            self.opcao = int(input('Escolha uma das opções acima: '))
            if self.opcao == 0:
                print("Obrigado!")
            if self.opcao == 1:
                self.coletar() #chamando o input
                print(f'A soma dos números é: {self.exer.somar(self.num1, self.num2)}')
            elif self.opcao == 2:
                self.coletar()  # chamando o input
                print(f'A subtração dos números digitados é: {self.exer.subtrair(self.num1, self.num2)}')
            elif self.opcao == 3:
                self.coletar()  # chamando o input
                print(f'A divisão dos números digitados é: {self.exer.dividir(self.num1, self.num2)}')
            elif self.opcao == 4:
                self.coletar()  # chamando o input
                print(f'A multiplicação dos números digitados é: {self.exer.multiplicar(self.num1, self.num2)}')
            elif self.opcao == 5:
                self.coletar()  # chamando o input
                print(f'A potência dos números digitados é: {self.exer.potencia(self.num1, self.num2)}')
            elif self.opcao == 6:
                self.coletar()  # chamando o input
                print(f'A raiz de {self.num1} digitado é: {self.exer.raiz(self.num1)}')
            elif self.opcao == 7:
                self.coletar()  # chamando o input
                print(f'A tabuada de {self.num1} digitado é: {self.exer.tabuada(self.num1)}')
            elif self.opcao == 8:
                print(self.exer.imprimir())
            elif self.opcao == 9:
                print(self.exer.imprimirpa())
            elif self.opcao == 10:
                print(self.exer.cemnum())
            elif self.opcao == 10:
                print(self.exer.cemnum())
            elif self.opcao == 11:
                print(self.exer.divisores())
            elif self.opcao == 12:
                self.coletar()  # chamando o input
                print(f' {self.exer.imppar(self.num1)}')
            elif self.opcao == 13:
                self.coletar()  # chamando o input
                print(f' {self.exer.desc(self.num1)}')
            elif self.opcao == 14:
                self.coletar()  # chamando o input
                print(f' {self.exer.numusu(self.num1)}')
            elif self.opcao == 15:
                self.coletar()  # chamando o input
                print(f' {self.exer.imprimirate(self.num1)}')
            elif self.opcao == 16:
                self.coletar()  # chamando o input
                print(f' {self.exer.somarate(self.num1)}')
            elif self.opcao == 17:
                self.coletar()  # chamando o input
                print(f'O fatorial do número é de:  {self.exer.fatorial(self.num1)}')
            elif self.opcao == 18:
                print(self.exer.primos())
            elif self.opcao == 19:
                self.coletar()  # chamando o input
                print(f'Os números primos são:  {self.exer.ehPrimo(self.num1)}')
            elif self.opcao == 20:
                self.coletar()  # chamando o input
                print(f'A sequência de Collatz é:  {self.exer.collatz(self.num1)}')
            elif self.opcao == 21:
                print(f'{self.exer.fibonnaci()}')
            elif self.opcao == 22:
                self.coletar()  # chamando o input
                print(f'A soma dos números é de:  {self.exer.somUsu(self.num1)}')
            elif self.opcao == 23:
                self.coletar()  # chamando o input
                print(f'  {self.exer.listPeI(self.num1)}')
            elif self.opcao == 24:
                self.coletar()  # chamando o input
                print(f'  {self.exer.imprimirPrimos(self.num1)}')
            elif self.opcao == 25:
                self.coletar()  # chamando o input
                print(f'  {self.exer.somIeP(self.num1)}')
            elif self.opcao == 26:
                self.coletar()  # chamando o input
                print(f'  {self.exer.ex1list2(self.num1, self.num2)}')
            elif self.opcao == 27:
                self.num1 = int(input('Informe o primeiro número:'))
                print(f'  {self.exer.ex2list2(self.num1)}')
            elif self.opcao == 28:
                self.coletar()  # chamando o input
                print(f'  {self.exer.ex3list2(self.num1, self.num2)}')
            elif self.opcao == 29:
                self.coletar2()
                print(f'Sua quantidade de dias:  {self.exer.ex4list2(self.num3, self.num4)}')
            elif self.opcao == 30:
                self.coletar3()
                print(f'{self.exer.ex5list2(self.num5, self.num6, self.num7,self.num8)}')
            elif self.opcao == 31:
                self.coletar3()
                print(f'{self.exer.ex6list2(self.num9)}')
            elif self.opcao == 32:
                self.coletar4()
                print(f'{self.exer.ex7list2(self.num10)}')
            elif self.opcao == 33:
                self.coletar5()
                print(f'{self.exer.ex8list2(self.num11, self.num12, self.num13)}')
            elif self.opcao == 34:
                self.num1 = int(input('Informe o primeiro número:'))
                print(f'{self.exer.ex9list2(self.num1)}')
            elif self.opcao == 35:
                print(f'{self.exer.ex10list2(self.num1)}')
            elif self.opcao == 36:
                self.coletar7()
                print(f'{self.exer.ex11list2(self.num25, self.num26)}')
            elif self.opcao == 37:
                self.coletar8()
                print(f'{self.exer.ex12list2(self.numero, self.saldo, self.debito, self.credito)}')
            elif self.opcao == 38:
                self.num1 = int(input('Informe o primeiro número:'))
                print(f'{self.exer.ex13list2(self.num1)}')
            elif self.opcao == 39:
                self.num1 = int(input('Informe o primeiro número:'))
                print(f'{self.exer.ex14list2(self.num1)}')
            elif self.opcao == 40:
                print(f'{self.exer.ex15list2(self.num1)}')
            elif self.opcao == 41:
                print(f'{self.exer.ex16list2(self.num1)}')
            elif self.opcao == 42:
                print(f'{self.exer.ex17list2(self.num1)}')
            elif self.opcao == 43:
                print(f'{self.exer.ex18list2(self.num1)}')
            elif self.opcao == 44:
                print(f'{self.exer.ex19list2(self.num1)}')





