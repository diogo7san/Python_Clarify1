import sqlite3

def conectarBanco():
    local = r"C:\Users\integral\Desktop\pythonDiogo\meuBanco.db"
    # com o "r", a \ não é interpretada, só o conteúdo.
    conexao = sqlite3.connect(local)
    return conexao

def criar_tabela():
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER   
        )
''')
    conexao.commit()
    conexao.close()

def inserir_usuarios(nome, idade):
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO Usuarios (nome, idade)
        VALUES (?, ?)
    ''', (nome, idade))
    conexao.commit()
    conexao.close()

def ver_usuarios():
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)
    conexao.close()
  
#Variável a gente guarda informação. Função a gente guarda código.
#Pra alterar o banco, precisa se comprometer. Pra ver, não precisa se comprometer. COMMIT



#criar_tabela()
inserir_usuarios("caio",    "37")
inserir_usuarios("Horacio", "36")
inserir_usuarios("Byanca",  "35")
inserir_usuarios("Juliana", "34")
inserir_usuarios("Diogo",   "33")
inserir_usuarios("Emanuel", "32")
inserir_usuarios("Marcelo", "31")
#ver_usuarios()