algoritmo "Multiplica��o de Matriz por Valor"
// Disciplina   : [Linguagem e L�gica de Programa��o] 
// Professor    : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 25/05/2023
var
   matriz: vetor[1..5, 1..5] de inteiro
   i, j, A: inteiro

inicio
   // Leitura dos elementos da matriz
   para i de 1 ate 5 faca
      para j de 1 ate 5 faca
         escreva("Digite o elemento da posicao [", i, ", ", j, "]: ")
         leia(matriz[i, j])
      fimpara
   fimpara

   // Leitura do valor A
   escreva("Digite o valor de A: ")
   leia(A)

   // Multiplica��o dos elementos da matriz por A
   para i de 1 ate 5 faca
      para j de 1 ate 5 faca
         matriz[i, j] <- matriz[i, j] * A
      fimpara
   fimpara

   // Impress�o dos elementos da matriz resultante
   escreval("Matriz resultante:")
   para i de 1 ate 5 faca
      para j de 1 ate 5 faca
         escreva(matriz[i, j], " ")
      fimpara
      escreval()
   fimpara

fimalgoritmo