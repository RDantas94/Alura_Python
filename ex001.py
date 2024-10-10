# Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar
# em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

'''Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
Terceiro Quadrante: os valores de x e y devem ser menores que zero;
Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
Caso contrário: o ponto está localizado no eixo ou origem.'''


def calcular_coordenadas():
    x = int(input('Digite o valor de x: '))
    y = int(input('Digite o valor de y: '))
    # Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
    if x > 0 and y > 0:
        return 'Primeiro quadrante'
    # Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
    elif x < 0 and y > 0:
        return 'Segundo quadrante'
    # Terceiro Quadrante: os valores de x e y devem ser menores que zero;
    elif x < 0 and y < 0:
        return 'Terceiro quadrante'
    # Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
    elif x > 0 and y < 0:
        return 'Quarto quadrante'
    # Caso contrário: o ponto está localizado no eixo ou origem.
    else:
        return 'O ponto está localizado no eixo ou origem.'


def main():
    calcular_coordenadas()


if __name__ == '__main__':
    main()
