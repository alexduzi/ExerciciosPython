# 4. Defina uma classe Circulo que pode ser construída a partir do seu raio.
# Essa classe deve possuir um método para calcular a sua área.
# 5. Escreva uma classe Polígono e duas classes derivadas, Retângulo e Triângulo que podem ser construidas passando largura e altura.
# Novamente as classes devem possuir um método para calcular a área.
# 6. Escreva uma função que recebe uma string com uma fita de DNA Ex "GATTACA" e retorna a fita complementar: "CTAATGT"
# 7. Escreva uma função que calcula o enésmo termo da sequência de Fibonacci (Fn = F(n-1) + F(n-2).
# 8. Escreva uma função que adiciona 2 números. a. Escreva uma função que recebe N números como parâmetros e retorna a soma.
# 9. Escreva uma função que recebe um número arbitrário de parâmetros de palavra chave e escreve na tela uma
# linha "parâmetro = valor" para cara parâmetro passado.
# 10. Use a biblioteca Turtle e escreva uma função recursiva que desenha um fractal.

# 1. Escreva uma função que mapeia uma uma lista de palavras numa lista de inteiros que representam o tamanho de cada palavra.
# Escreva essa função de 4 formas:
# a. Usando um loop for
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
    if ' ' in e:


def main():
    mostra_file();
    

if __name__ == '__main__':
    main()
    






 
