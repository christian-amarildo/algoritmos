
algoritmo "SomaElementosImpares"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor    : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 16/05/2023
var
   A: vetor[1..500] de real
   soma,termo: real
   i: inteiro

inicio
soma <- 1
para i de 1 ate 50 faca
    termo <- 1/(2*i)
    soma <- soma + termo
fimpara

escreva("A soma da sequ�ncia �: ", soma)

fimalgoritmo