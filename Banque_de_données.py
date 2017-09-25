import sqlite3

class Banque_de_données(object):
	"""docstring for Banque_de_données"""
	def __init__(self):
		self.verbes = list
		self.conn = sqlite3.connect('banco.bd')
		self.cursor = self.conn.cursor()
		self.cursor.execute("""CREATE TABLE IF NOT EXISTS Users(
								id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
								nome varchar(50),
								login varchar(10),
								senha varchar(10),
								best_score integer
							);""")

		self.cursor.execute("""CREATE TABLE IF NOT EXISTS Verbes(
								id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
								verbe varchar(50),
								dificulté varchar(10)
							);""")

		self.cursor.execute("""CREATE TABLE IF NOT EXISTS présent(
		 						id  INTEGER PRIMARY KEY,
		 						je varchar(50),
		 						tu varchar(50),
		 						il varchar(50),
		 						nous varchar(50),
		 						vous varchar(50),
		 						ils varchar(50)
		 					);""")

		self.cursor.execute("""CREATE TABLE IF NOT EXISTS Passé(
		 						id  INTEGER PRIMARY KEY,
		 						auxiliaire varchar(50),
		 						participe varchar(10)
		 					);""")

		self.cursor.execute("""CREATE TABLE IF NOT EXISTS Imparfait(
		 						id  INTEGER PRIMARY KEY,
		 						je varchar(50),
		 						tu varchar(50),
		 						il varchar(50),
		 						nous varchar(50),
		 						vous varchar(50),
		 						ils varchar(50)
		 					);""")

		self.cursor.execute("""CREATE TABLE IF NOT EXISTS Futur(
		 						id  INTEGER PRIMARY KEY,
		 						je varchar(50),
		 						tu varchar(50),
		 						il varchar(50),
		 						nous varchar(50),
		 						vous varchar(50),
		 						ils varchar(50)
		 					);""")								
		a = "medium"
		self.cursor.execute("UPDATE Verbes SET dificulté = ? WHERE id = 9", (a,))						
		self.conn.commit()

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

	def lister_verbes(self):
		sql_query = 'SELECT * FROM Verbes'
		for row in self.cursor.execute(sql_query):
			print(row)

		input("Prêt?")

	def Ajouter_verbe(self):
		v = input("Le nom du verbe:")
		dif = input("La dificulté:")
		
		#Regarde si le verbe est dejá dans la table
		sql_query = "SELECT * FROM Verbes WHERE verbe = ?"
		self.cursor.execute(sql_query, (v,))
		l = self.cursor.fetchone()
		if(l == None):
			self.cursor.execute("""INSERT INTO Verbes (verbe, dificulté) VALUES (?,?)""", (v, dif))
		else:
			print("Ce verbe est dejá dans la table!")

		self.conn.commit()
		input("Prêt?")

	def Ajouter_conjugaison(self):
		v = input("Le nom du verbe:")
		
		#Regarde si le verbe est dans la table
		sql_query = "SELECT * FROM Verbes WHERE verbe = ?"
		self.cursor.execute(sql_query, (v,))
		l = self.cursor.fetchone()

		if(l == None):
			print("Ce verbe n'est pas dans la table!")

		else:
			temp = input("Le temp verbel(présent,passé,imparfait, futur):")

			if(temp == "présent"):
				print("Conjuguez ce verbe")
				je = input("je:")
				tu = input("tu:")
				il = input("il:")
				nous = input("nous:")
				vous = input("vous:")
				ils = input("ils:")
				
				sql_query = "INSERT INTO présent(id, je, tu, il, nous, vous, ils) VALUES (?, ?, ?, ?, ?, ?, ?)"
				self.cursor.execute(sql_query, (l[0], je, tu, il, nous, vous, ils))

			elif(temp == "passé"):
				print("passé")

			elif(temp == "imparfait"):
				print("imp")

			elif(temp == "futur"):
				print("f")

			else:
				print("Nop")

		input("Prêt?")
		self.conn.commit()

	def lister_table(self):	
		t = input("Table: ")
		sql_query = "SELECT * FROM "
		for row in self.cursor.execute(sql_query+t):
			print(row)

		input("Prêt?")

	def close(self):
		self.conn.close()

		