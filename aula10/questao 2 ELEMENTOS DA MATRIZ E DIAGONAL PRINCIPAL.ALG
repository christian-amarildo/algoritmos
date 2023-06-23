algoritmo "Elementos da Matriz e Diagonal Principal"
// Disciplina   : [Linguagem e Lógica de Programação] 
// Professor    : Antonio Carlos Nicolodi 
// Descrição   : Desenvolva um algoritmo que leia os elementos de uma matriz
// 5x5, imprima na tela todos os elementos da matriz, e depois
// imprima os elementos da diagonal principal.
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 25/05/2023

var
   matriz: vetor[1..5, 1..5] de inteiro
   i, j: inteiro

inicio
   // Leitura dos elementos da matriz
   para i de 1 ate 5 faca
      para j de 1 ate 5 faca
         escreva("Digite o elemento da posicao [", i, ", ", j, "]: ")
         leia(matriz[i, j])
      fimpara
   fimpara

   // Impressão de todos os elementos da matriz
   escreval("Elementos da matriz:")
   para i de 1 ate 5 faca
      para j de 1 ate 5 faca
         escreva(matriz[i, j], " ")
      fimpara
      escreval()
   fimpara

   // Impressão dos elementos da diagonal principal
   escreval("Elementos da diagonal principal:")
   para i de 1 ate 5 faca
      escreva(matriz[i, i], " ")
   fimpara

fimalgoritmo