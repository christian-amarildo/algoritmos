algoritmo "Somat�rio de Matriz"
// Disciplina   : [Linguagem e L�gica de Programa��o] 
// Professor    : Antonio Carlos Nicolodi 
// Descri��o   : Elabore um algoritmo que leia os elementos de uma matriz 5 X
// 5 e imprima na tela o somat�rio de todos os elementos da
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

   // C�lculo do somat�rio dos elementos da matriz
   soma <- 0
   para i de 1 ate 5 faca
      para j de 1 ate 5 faca
         soma <- soma + matriz[i, j]
      fimpara
   fimpara

   // Impress�o do somat�rio
   escreval("O somatorio dos elementos da matriz e: ", soma)

fimalgoritmo