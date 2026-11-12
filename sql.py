import sqlite3

# EXERCÍCIO 1

conn = sqlite3.connect("loja.db")
cursor = conn.cursor()

cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos(
        id INTEGER PRIMARY KEY,
        nome TEXT,
        categoria TEXT,
        preco REAL,
        quantidade INTEGER)
    """)

cursor.execute("""
    INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES
    ("Monitor", "Informática", 200, 10),
    ("Teclado Mecânico", "Informática", 150, 25),
    ("Mouse Gamer", "Informática", 90, 40),
    ("Headset", "Áudio", 120, 18),
    ("Cadeira Ergonômica", "Móveis", 650, 6),
    ("Webcam Full HD", "Informática", 180, 15),
    ("Caixa de Som Bluetooth", "Áudio", 220, 12),
    ("Mesa para Computador", "Móveis", 480, 8)
    """)

cursor.execute("""
    SELECT * FROM produtos
    """)
print(cursor.fetchall())

cursor.execute("""
    SELECT nome, preco FROM produtos
    """)
print(cursor.fetchall())

cursor.execute("""
    UPDATE produtos SET preco = ? WHERE nome = ?
    """, (250, "Monitor"))

cursor.execute("""
    UPDATE produtos SET quantidade = ? WHERE nome = ?
    """, (20, "Monitor"))

cursor.execute("""
    DELETE FROM produtos WHERE id = 3
    """)

cursor.execute("""
    SELECT * FROM produtos
    """)
print(cursor.fetchall())

conn.commit()
conn.close()