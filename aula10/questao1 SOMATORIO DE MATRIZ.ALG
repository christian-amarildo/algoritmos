algoritmo "Somatório de Matriz"
// Disciplina   : [Linguagem e Lógica de Programação] 
// Professor    : Antonio Carlos Nicolodi 
// Descrição   : Elabore um algoritmo que leia os elementos de uma matriz 5 X
// 5 e imprima na tela o somatório de todos os elementos da
// matriz
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 25/05/2023
var
   matriz: vetor[1..5, 1..5] de inteiro
   i, j, soma: inteiro

inicio
   // Leitura dos elementos da matriz
   para i de 1 ate 5 faca
      para j de 1 ate 5 faca
         escreva("Digite o elemento da posicao [", i, ", ", j, "]: ")
         leia(matriz[i, j])
      fimpara
   fimpara

   // Cálculo do somatório dos elementos da matriz
   soma <- 0
   para i de 1 ate 5 faca
      para j de 1 ate 5 faca
         soma <- soma + matriz[i, j]
      fimpara
   fimpara

   // Impressão do somatório
   escreval("O somatorio dos elementos da matriz e: ", soma)

fimalgoritmo