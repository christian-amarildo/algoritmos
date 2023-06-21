
algoritmo "SomaElementosImpares"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor    : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 16/05/2023
var
   A: vetor[1..5] de real
   soma: real
   i: inteiro

inicio
   soma <- 0

   // Leitura dos elementos do vetor A
   para i de 1 ate 5 faca
      escreva("Digite o elemento ", i, ": ")
      leia(A[i])
   fimpara

   // Cálculo da soma dos elementos nas posições ímpares
   para i de 1 ate 5 passo 2 faca
      soma <- soma + A[i]
   fimpara

   // Apresentação do resultado
   escreva("A soma dos elementos nas posições ímpares é: ", soma)

fimalgoritmo
