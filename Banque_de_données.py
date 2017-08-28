import sqlite3

class Banque_de_données(object):
	"""docstring for Banque_de_données"""
	def __init__(self):
		self.conn = sqlite3.connect('banco.bd')
		self.cursor = self.conn.cursor()
		self.cursor.execute("""CREATE TABLE IF NOT EXISTS Users(
								id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
								nome varchar(50),
								login varchar(10),
								senha varchar(10),
								best_score integer
							);""")

	def creer_compt(self, prenom, usr, psw):
		self.cursor.execute("""INSERT INTO Users (nome,login,senha,best_score) VALUES (?,?,?,0)""", (prenom,usr,psw))
		self.conn.commit()

	def login(self, usr, psw):
		self.cursor.execute("""SELECT nome,senha FROM Users WHERE login = ?""", (usr,))
		l = self.cursor.fetchone()
		if(l[1] == psw):
			return (True,l[0])
		else:
			return (False,"")

	def lister_utilisateurs(self):
		sql_query = 'SELECT login, best_score FROM Users'
		for row in self.cursor.execute(sql_query):
			print(row)

		input("Prêt?")

	def close(self):
		self.conn.close()

		