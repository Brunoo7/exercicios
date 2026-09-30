# EXERCÍCIO 1
# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

# p1 = Pessoa("Bruno", 18)
# p2 = Pessoa("Ana", 30)

# print(f"Nome: {p1.nome}")
# print(f"Idade: {p1.idade}")
# print(f"Nome: {p2.nome}")
# print(f"Idade: {p2.idade}")

# EXERCÍCIO 2
# class Carro:
#     def __init__(self, marca, modelo, ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano
#     def exibir_infos(self):
#         print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")

# c1 = Carro("Chevrolet", "Onix", 2023)
# c2 = Carro("Toyota", "Hilux", 2022)
# c3 = Carro("Volkswagen", "Gol", 2021)

# c1.exibir_infos()
# c2.exibir_infos()
# c3.exibir_infos()

# EXERCÍCIO 3
class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    def exibir_infos(self):
        print(f"Produto: {self.nome}, Preço: {self.preco}, estoque: {self.estoque}")

p1 = Produto("Teclado", 150, 50)

p1.exibir_infos()
        