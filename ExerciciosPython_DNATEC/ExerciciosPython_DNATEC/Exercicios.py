
# 1. Escreva uma função que mapeia uma uma lista de palavras numa lista de inteiros que representam o tamanho de cada palavra.
# Escreva essa função de 4 formas:
# a. Usando um loop for

from math import *
import string
from turtle import *

def lista_palavras_for():
    palavras = ["Palavra1", "Palavra_2", "segunda-feira", "celular", "cidade"]
    tamanhoPalavras = []
    for palavra in palavras:
        tamanhoPalavras.append(len(palavra))
    for tamanho in tamanhoPalavras:
        print tamanho
# b. Usando a função map
def lista_palavras_map():
    palavras = ["Palavra1", "Palavra_2", "segunda-feira", "celular", "cidade"]
    tamanhoPalavras = map(len, palavras)
    for tamanho in tamanhoPalavras:
        print tamanho
# c. Usando list comprehensions
def lista_palavras_list_comprehensions():
    palavras = ["Palavra1", "Palavra_2", "segunda-feira", "celular", "cidade"]
    tamanhoPalavras = [len(palavra) for palavra in palavras]
    for tamanho in tamanhoPalavras:
        print tamanho
# d. Usando dict comprehensions
def lista_palavras_dict_comprehensions():
    palavras = ["Palavra1", "Palavra_2", "segunda-feira", "celular", "cidade"]
    tamanhoPalavras = {len(palavra): palavra for palavra in palavras}
    for tamanho in tamanhoPalavras:
        print "Tamanho: %s --- palavra: %s" %(str(tamanho), tamanhoPalavras[tamanho])


# 2. Escreva uma função que recebe o nome de um filme e escreve na uma frase como esta:
# "Meu filme favorito é La Belle Verte". Essa função deve ter o valor default do nome do filme "La Belle Verte".
def mostra_file(filme = "La Belle Verte"):
    if(filme == "La Belle Verte"):
        print "Meu filme favorito eh %s" %filme
    else:
        print "Meu filme favorito eh %s " %filme

# 3. Escreva uma função de 'correção ortográfica' simplificada que recebe uma string e:
# a. Se houver mais de um espaço entre as palavras, substitua-o por um .
# b. Insere um espaço depois do ponto se o ponto estiver justaposto a palavra Ex: corrige("Frase a ser corrida.Outra frase.") ->
# "Frase a ser corrigida. Outra Frase"
def correcao_ortografica(e):
    if e.count(' ') > 1:
        new = e.replace(' ','.', e.count(' '))

    correcao = ''
    ponto = False
    for n in range(len(new)):
        if new[n] == '.':
            ponto = True
        if  ponto and new[n].isalpha():
            ponto = False
            correcao += ' '
        correcao += new[n]
        
    print correcao

# 4. Defina uma classe Circulo que pode ser construída a partir do seu raio.
# Essa classe deve possuir um método para calcular a sua área.
class Circulo(object):
    def __init__(self, raio):
        self.raio = raio
    def calcular_area(self):
        return self.raio**2 * pi


# 5. Escreva uma classe Polígono e duas classes derivadas, Retângulo e Triângulo que podem ser construidas passando largura e altura.
# Novamente as classes devem possuir um método para calcular a área.
class Poligono(object):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    def calcular_area(self):
        pass

class Retangulo(Poligono):
    def calcular_area(self):
        return self.altura * self.largura

class Triangulo(Poligono):
    def calcular_area(self):
        return (self.altura * self.largura) / 2


# 6. Escreva uma função que recebe uma string com uma fita de DNA Ex "GATTACA" e retorna a fita complementar: "CTAATGT"
def fita_complementar(string):
    complemento = {'A':'T','T':'A','G':'C','C':'G'}
    return "".join([complemento[dna] for dna in reversed(string)])


# 7. Escreva uma função que calcula o enésmo termo da sequência de Fibonacci (Fn = F(n-1) + F(n-2).
def fibonacci(enesimo):
    if enesimo == 0:
        return 0
    elif enesimo == 1:
        return 1
    else:
        return fibonacci(enesimo-1)+fibonacci(enesimo-2)


# 8. Escreva uma função que adiciona 2 números.
# a. Escreva uma função que recebe N números como parâmetros e retorna a soma.
def soma_numeros(*args):
    return sum(n for n in args)

# 9. Escreva uma função que recebe um número arbitrário de parâmetros de palavra chave e escreve na tela uma
# linha "parâmetro = valor" para cara parâmetro passado.
def mostra_parametros(**kwargs):
    for key, value in kwargs.items():
        print '%s = %s' %(str(key), str(value))

# 10. Use a biblioteca Turtle e escreva uma função recursiva que desenha um fractal.
def fractal(length, depth):
   if depth == 0:
     forward(length)
   else:
     fractal(length/5, depth-1)
     right(60)
     fractal(length/5, depth-1)
     left(120)
     fractal(length/5, depth-1)
     right(60)
     fractal(length/5, depth-1)




def main():
    fractal(700, 3)


if __name__ == '__main__':
    main()









