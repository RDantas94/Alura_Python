
# 1) Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:

    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

# Instanciando um carro e atribuindo valores aos seus atributos


meu_carro = Carro(modelo='Celta', cor='Cinza', ano=2011)

# 2) Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.


class Restaurante:
    def __init__(self, nome, categoria, ativo, entrega, nota_avaliacao):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.entrega = entrega
        self.nota_avaliacao = nota_avaliacao

# Instanciando um restaurante e atribuindo valores aos seus atributos


restaurante_exemplo = Restaurante(
    nome='Cometa', categoria='Gourmet', ativo=True, entrega=True, nota_avaliacao=4.5)

# 3) Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão.


class Restaurante:
    def __init__(self, nome, categoria, entrega, nota_avaliacao, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.entrega = entrega
        self.nota_avaliacao = nota_avaliacao


#  Crie uma instância utilizando o construtor.

novo_restaurante = Restaurante(nome='Bom de garfo', categoria='Fast Food')

# 4) Adicione um método especial `__str__` à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria.
# Exiba essa mensagem para uma instância de restaurante.


class Restaurante:
    def __init__(self, nome, categoria, entrega, nota_avaliacao, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.entrega = entrega
        self.nota_avaliacao = nota_avaliacao

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

# Exiba essa mensagem para uma instância de restaurante.


restaurante_especial = Restaurante(
    nome='Popular', categoria='Self-Service', entrega=False, nota_avaliacao=5)
print(restaurante_especial)

# 5) Crie uma classe chamada `Cliente` e pense em 4 atributos.


class Cliente:
    def __init__(self, nome='', idade=0, profissao='', cartao_fidelidade=False):
        self.nome = nome
        self._idade = idade
        self._profissao = profissao
        self._cartao_fidelidade = cartao_fidelidade


# Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
cliente1 = Cliente(nome='Rafael', idade=29,
                   profissao='Estudante', cartao_fidelidade=True)
cliente2 = Cliente(nome='Camilla', idade=24,
                   profissao='Estudante', cartao_fidelidade=False)
cliente3 = Cliente(nome='Carlos', idade=60,
                   profissao='Engenheiro', cartao_fidelidade=False)
