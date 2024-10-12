from modelos.cardapio.cardapio import ItemCardapio


class Bebida(ItemCardapio):
    def __init__(self, name, preco, tamanho):
        super().__init__(name, preco)
        self.tamanho = tamanho

    def __str__(self):
        return self._nome

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)
