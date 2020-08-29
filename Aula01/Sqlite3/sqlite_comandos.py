
import sqlite3
conexao = sqlite3.connect(r"C:\Users\14745\Documents\AulaPython_Martina\Aula01\Sqlite3\pesquisa.bd") #Cria o banco de dados
cursor = conexao.cursor() # Cria um cursor

cliente = """CREATE TABLE Clientes (
	id INTEGER NOT NULL,
	nome TEXT,
	cpf TEXT,
	telefone TEXT,
	email TEXT,
	id_endereco INTEGER,
	CONSTRAINT Clientes_PK PRIMARY KEY (id),
	CONSTRAINT Clientes_FK FOREIGN KEY (id_endereco) REFERENCES Endereco(id)
);
"""

endereco = '''CREATE TABLE Endereco (
	id INTEGER NOT NULL,
	rua TEXT,
	complemento TEXT,
	numero INTEGER,
	bairro TEXT,
	cidade INTEGER,
	CONSTRAINT Endereco_PK PRIMARY KEY (id)
);
'''
respostas = '''
CREATE TABLE Respostas (
	id INTEGER NOT NULL,
	pergunta1 TEXT,
	pergunta2 TEXT,
	pergunta4 TEXT,
	pergunta TEXT,
	id_cliente INTEGER NOT NULL,
	CONSTRAINT Respostas_PK PRIMARY KEY (id),
	CONSTRAINT Respostas_FK FOREIGN KEY (id_cliente) REFERENCES Clientes(id)
);'''


cursor.execute(endereco) # Carrega o comando sql
conexao.commit() # Aplica o comando sql
cursor.execute(cliente)
conexao.commit()
cursor.execute(respostas)
conexao.commit()

conexao.close()