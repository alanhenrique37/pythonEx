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
              "\n29. Idade em dias"

              )

    def coletar(self):
        self.num1 = int(input('Informe o primeiro número:'))
        self.num2 = int(input('Informe o segundo número:'))

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
                self.num1 = int(input('Informe o primeiro número:'))
                print(f'Sua quantidade de dias:  {self.exer.ex4list2(self.num1)}')



