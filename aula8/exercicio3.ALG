Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o] 
// Professor    : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 16/05/2023

var
   numeros: vetor[1..10] de inteiro
   soma, media: real
   maior, menor, valor: inteiro
   i, count: inteiro

inicio
   soma <- 0
   maior <- 0
   menor <- 20
   count <- 0

   para i de 1 ate 10 faca
         escreva("Digite um n�mero par entre 1 e 20: ")
         leia(valor)
         se (valor % 2 = 0) e (valor >= 1) e (valor <= 20) entao
            numeros[count + 1] <- valor
            count <- count + 1
         fimse

soma <- soma + valor

   se valor > maior entao
      maior <- valor

   se valor < menor entao
      menor <- valor

   fimpara

   media <- soma / count

   escreva("Valores:")
   para i de 1 ate count faca
      escreva(numeros[i])
   fimpara

   escreva("M�dia dos valores:", media)
   escreva("Maior valor:", maior)
   escreva("Menor valor:", menor)

fimalgoritmo
