
algoritmo "SomaElementosImpares"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor    : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
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

   // C�lculo da soma dos elementos nas posi��es �mpares
   para i de 1 ate 5 passo 2 faca
      soma <- soma + A[i]
   fimpara

   // Apresenta��o do resultado
   escreva("A soma dos elementos nas posi��es �mpares �: ", soma)

fimalgoritmo
