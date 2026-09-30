# EXERCÍCIO 1
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("Bruno", 18)
p2 = Pessoa("Ana", 30)

print(f"Nome: {p1.nome}")
print(f"Idade: {p1.idade}")
print(f"Nome: {p2.nome}")
print(f"Idade: {p2.idade}")