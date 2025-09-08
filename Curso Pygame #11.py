class Cachorros:
    def __init__(self,nome, cor_de_pelo, idade, tamanho):
        self.nome = nome
        self.cor_de_pelo = cor_de_pelo
        self.idade = idade
        self.tamanho = tamanho
    def latir(self):
        print('au au')

cachorro_1 = Cachorros('Toby', 'marrom cocô', 5, 'grande')

print(cachorro_1.nome)