import sqlite3

# EXERCÍCIO 1

# conn = sqlite3.connect("loja.db")
# cursor = conn.cursor()

# cursor.execute("""
#         CREATE TABLE IF NOT EXISTS produtos(
#         id INTEGER PRIMARY KEY,
#         nome TEXT,
#         categoria TEXT,
#         preco REAL,
#         quantidade INTEGER)
#     """)

# cursor.execute("""
#     INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES
#     ("Monitor", "Informática", 200, 10),
#     ("Teclado Mecânico", "Informática", 150, 25),
#     ("Mouse Gamer", "Informática", 90, 40),
#     ("Headset", "Áudio", 120, 18),
#     ("Cadeira Ergonômica", "Móveis", 650, 6),
#     ("Webcam Full HD", "Informática", 180, 15),
#     ("Caixa de Som Bluetooth", "Áudio", 220, 12),
#     ("Mesa para Computador", "Móveis", 480, 8)
#     """)

# cursor.execute("""
#     SELECT * FROM produtos
#     """)
# print(cursor.fetchall())

# cursor.execute("""
#     SELECT nome, preco FROM produtos
#     """)
# print(cursor.fetchall())

# cursor.execute("""
#     UPDATE produtos SET preco = ? WHERE nome = ?
#     """, (250, "Monitor"))

# cursor.execute("""
#     UPDATE produtos SET quantidade = ? WHERE nome = ?
#     """, (20, "Monitor"))

# cursor.execute("""
#     DELETE FROM produtos WHERE id = 3
#     """)

# cursor.execute("""
#     SELECT * FROM produtos
#     """)
# print(cursor.fetchall())

# conn.commit()
# conn.close()

# EXERCÍCIO 2
# conn = sqlite3.connect("loja.db")
# cursor = conn.cursor()

# cursor.execute("""
#     SELECT * FROM produtos WHERE preco > 100;
#     """)
# print(cursor.fetchall())

# cursor.execute("""
#     SELECT * FROM produtos WHERE quantidade < 10;
#     """)
# print(cursor.fetchall())

# cursor.execute("""
#     SELECT * FROM produtos WHERE categoria = "Informática";
#     """)
# print(cursor.fetchall())

# cursor.execute("""
#     SELECT * FROM produtos WHERE nome LIKE "%Mouse%";
#     """)
# print(cursor.fetchall())

# cursor.execute("""
#     SELECT SUM(preco * quantidade) FROM produtos;
#     """)
# print(cursor.fetchall())

# cursor.execute("""
#     SELECT COUNT(id) FROM produtos;
#     """)
# print(cursor.fetchall())

# cursor.execute("""
#     SELECT MAX(preco) FROM produtos;
#     """)
# print(cursor.fetchall())

# cursor.execute("""
#     SELECT MIN(preco) FROM produtos;
#     """)
# print(cursor.fetchall())

# cursor.execute("""
#     SELECT categoria, COUNT (Nome) FROM produtos GROUP BY categoria DESC;
#     """)
# print(cursor.fetchall())

# cursor.execute("""
#     SELECT nome, preco FROM produtos ORDER BY preco;
#     """)
# print(cursor.fetchall())

# cursor.execute("""
#     SELECT * FROM produtos WHERE preco BETWEEN 100 AND 300;
#     """)
# print(cursor.fetchall())

# EXERCÍCIO 3
conn = sqlite3.connect("loja_02.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes(
    id INTEGER PRIMARY KEY,
    nome TEXT,
    email TEXT,
    cidade TEXT)
    """)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos(
    id INTEGER PRIMARY KEY,
    nome TEXT,
    preco REAL,
    quantidade INTEGER)
    """)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS vendas(
    id INTEGER PRIMARY KEY,
    cliente_id INTEGER,
    produto_id INTEGER,
    quantidade INTEGER,
    data_venda TEXT,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
    )
    """)

cursor.execute("DELETE FROM vendas")
cursor.execute("DELETE FROM produtos")
cursor.execute("DELETE FROM clientes")

cursor.execute("""
    INSERT INTO clientes (nome, email, cidade) VALUES
    ("Ana Souza", "ana.souza@email.com", "Osasco"),
    ("Carlos Lima", "carlos.lima@email.com", "São Paulo"),
    ("Mariana Costa", "mariana.costa@email.com", "Barueri"),
    ("Pedro Alves", "pedro.alves@email.com", "Carapicuíba"),
    ("Juliana Rocha", "juliana.rocha@email.com", "Santana de Parnaíba")
    """)

cursor.execute("""
    INSERT INTO produtos (nome, preco, quantidade) VALUES
    ("Teclado Mecânico", 249.90, 30),
    ("Mouse Gamer", 129.90, 50),
    ("Monitor", 899.00, 15),
    ("Headset", 199.90, 25),
    ("Webcam HD", 159.90, 20),
    ("Cabo HDMI", 29.90, 100),
    ("Mousepad Grande", 59.90, 40),
    ("SSD 480GB", 279.90, 18)
    """)

cursor.execute("""
    INSERT INTO vendas (cliente_id, produto_id, quantidade, data_venda) VALUES
    (1, 1, 1, "2026-11-01"),
    (2, 3, 2, "2026-11-02"),
    (3, 2, 1, "2026-11-02"),
    (4, 6, 3, "2026-11-03"),
    (5, 8, 1, "2026-11-04"),
    (1, 4, 1, "2026-11-05"),
    (2, 7, 2, "2026-11-06"),
    (3, 5, 1, "2026-11-08"),
    (4, 1, 1, "2026-11-09"),
    (5, 2, 2, "2026-11-10"),
    (1, 6, 4, "2026-11-11"),
    (2, 8, 1, "2026-11-12")
    """)

cursor.execute("""
    SELECT clientes.nome AS cliente, produtos.nome AS produtos FROM vendas INNER JOIN clientes ON vendas.cliente_id = cliente_id INNER JOIN produtos ON vendas.produto_id = produto_id
    """)
print(cursor.fetchall())