# 1 - Crie uma lista para cada informação a seguir:

'''Lista de números de 1 a 10;
Lista com quatro nomes;
Lista com o ano que você nasceu e o ano atual.'''
lista_numeros = list(range(11))
lista_nomes = ['Rafael', 'Gustavo', 'Matheus', 'Roberta']
lista_anos = [1994, 2024]

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
lista_times = ['Cariocas', 'Tinguá', 'Papucaia',
               'Niterói', 'Piranema', 'Latinos']
for time in lista_times:
    print(time)

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
soma_impares = 0
for i in range(1, 11):
    if i % 2 != 0:
        soma_impares += i
print(f'A soma dos números ímpares de 1 a 10 é {soma_impares}')

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
for i in range(1, 11)[::-1]:
    print(i)
# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
# já realizado no curso em vídeo

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
numeros = [1, 2, 3, 4, 'cinco', 6, 7]

soma_total = 0

for num in numeros:
    try:
        soma_total += num
    except TypeError:
        print(f"Não foi possível somar o valor '{
              num}' porque não é um número.")

print(f'A soma dos números válidos é {soma_total}')

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
numeros = [10, 20, 30, 40, 50]

try:
    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade
    print(f'A média dos valores é {media:.2f}')
except ZeroDivisionError:
    print("Erro: Não é possível calcular a média de uma lista vazia.")
