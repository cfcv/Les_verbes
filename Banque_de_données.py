import sqlite3
import random
import os
from datetime import datetime

class Banque_de_données(object):
	"""docstring for Banque_de_données"""
	def __init__(self):
		self.c = False
		self.verbes = list()
		self.conn = sqlite3.connect('banco.bd')
		self.cursor = self.conn.cursor()
		self.cursor.execute("""CREATE TABLE IF NOT EXISTS Users(
								id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
								login varchar(10),
								nome varchar(50),
								senha varchar(10),
								scorePre integer,
								scorePass interger,
								scoreImp integer,
								scoreFutur integer,
								scoreSubj integer,
								lastdate varchar(100)		
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

		self.cursor.execute("""CREATE TABLE IF NOT EXISTS Subjonctif(
								id  INTEGER PRIMARY KEY,
		 						je varchar(50),
		 						tu varchar(50),
		 						il varchar(50),
		 						nous varchar(50),
		 						vous varchar(50),
		 						ils varchar(50)
								);""")

		self.cursor.execute("""CREATE TABLE IF NOT EXISTS Erreurs(
		 						 id INTEGER PRIMARY KEY, 
		 						 present INTEGER,
		 						 passe INTEGER,
		 						 imparfait INTEGER,
		 						 futur INTEGER,
								 subjonctif INTEGER 
		 						 );""")
		self.pronoms = list(["Je", "Tu", "Il", "Nous", "Vous", "Ils"])

	def inicializa_score(self):
		self.cursor.execute("UPDATE Users SET scorePre = 0, scorePass = 0, scoreImp = 0, scoreFutur = 0, scoreSubj = 0")

	def inicializa_words(self, temp):
		sql_query = "SELECT * FROM Verbes WHERE id = ?"
		del self.verbes[0:len(self.verbes)]
		self.index = list()
		self.c = False

		if(temp == "présent"):
			for row in self.cursor.execute("SELECT id,present FROM Erreurs ORDER BY present DESC"):
				self.index.append(row)

		elif(temp == "passé composé"):
			for row in self.cursor.execute("SELECT id,passe FROM Erreurs ORDER BY passe DESC"):
				self.index.append(row)

		elif(temp == "imparfait"):
			for row in self.cursor.execute("SELECT id,imparfait FROM Erreurs ORDER BY imparfait DESC"):
				self.index.append(row)

		elif(temp == "futur"):
			for row in self.cursor.execute("SELECT id,futur FROM Erreurs ORDER BY futur DESC"):
				self.index.append(row)
		
		elif(temp == "subjonctif"):
			for row in self.cursor.execute("SELECT id,subjonctif FROM Erreurs ORDER BY subjonctif DESC"):
				self.index.append(row)
		
		#print(self.index)
		for i in range(0,len(self.index)):
			self.cursor.execute(sql_query, (self.index[i][0], ))
			l = self.cursor.fetchone()
			aux = (self.index[i][1],)
			l = l+aux
			self.verbes.append(l)
		#Debug
		print(self.verbes)

	def inicializa_erreurs(self):
		#for i in range(1,78):
		#	sql_query = "SELECT id FROM Erreurs WHERE id = ?"
		#	self.cursor.execute(sql_query, (i, ))
		#	l = self.cursor.fetchone()
		#	if(l == None):
		#		self.cursor.execute("INSERT INTO Erreurs (id,present,passe,imparfait,futur) VALUES (?,0,0,0,0)", (i,))
		#self.conn.commit()
		#input("a")
		self.cursor.execute("UPDATE Erreurs SET subjonctif = 0")
		#for i in range(1,78):
		#	sql_query = "SELECT * FROM Erreurs WHERE id = ?"
		#	self.cursor.execute(sql_query, (i, ))
		#	l = self.cursor.fetchone()
		#	print(l[5])
		#input("b")

	def creer_compt(self, prenom, usr, psw):
		self.cursor.execute("""INSERT INTO Users (nome,login,senha,scorePre,scorePass,scoreImp,scoreFutur) VALUES (?,?,?,0,0,0,0)""", (prenom,usr,psw))
		self.conn.commit()

	def login(self, usr, psw):
		self.cursor.execute("""SELECT * FROM Users WHERE login = ?""", (usr,))
		l = self.cursor.fetchone()
		if(l[3] == psw):
			data = datetime.now()
			return (True,l[2], l[4], l[5], l[6], l[7], l[9], usr, data)
		else:
			return (False,"")

	def lister_utilisateurs(self):
		sql_query = 'SELECT * FROM Users'
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
			temp = input("Le temp verbel(présent,passé,imparfait, futur, subjonctif):")

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
				aux = input("Quel est le auxiliaire utilise avec ce verbe: ")
				participe = input("Quel est le participe passé de ce verbe:")

				sql_query = "INSERT INTO Passé(id, auxiliaire, participe) VALUES (?, ?, ?)"
				self.cursor.execute(sql_query, (l[0], aux, participe))

			elif(temp == "imparfait"):
				print("Conjuguez ce verbe")
				je = input("je:")
				tu = input("tu:")
				il = input("il:")
				nous = input("nous:")
				vous = input("vous:")
				ils = input("ils:")
				
				sql_query = "INSERT INTO Imparfait(id, je, tu, il, nous, vous, ils) VALUES (?, ?, ?, ?, ?, ?, ?)"
				self.cursor.execute(sql_query, (l[0], je, tu, il, nous, vous, ils))

			elif(temp == "futur"):
				print("Conjuguez ce verbe")
				je = input("je:")
				tu = input("tu:")
				il = input("il:")
				nous = input("nous:")
				vous = input("vous:")
				ils = input("ils:")
				
				sql_query = "INSERT INTO Futur(id, je, tu, il, nous, vous, ils) VALUES (?, ?, ?, ?, ?, ?, ?)"
				self.cursor.execute(sql_query, (l[0], je, tu, il, nous, vous, ils))

			elif(temp == "subjonctif"):
				print("Conjuguez ce verbe")
				je = input("je:")
				tu = input("tu:")
				il = input("il:")
				nous = input("nous:")
				vous = input("vous:")
				ils = input("ils:")
				
				sql_query = "INSERT INTO Subjonctif(id, je, tu, il, nous, vous, ils) VALUES (?, ?, ?, ?, ?, ?, ?)"
				self.cursor.execute(sql_query, (l[0], je, tu, il, nous, vous, ils))

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

	def random_word(self):
		tamanho = len(self.verbes)
		print(self.verbes)
		print("tamanho atual:",tamanho)
		if(tamanho > 0):
			if(self.c):
				aux = random.randint(0,len(self.verbes)-1)
				print("random:",aux)
				return (True,self.verbes.pop(aux))
			
			else:
				l = self.verbes[0][3]
				if(l == 0):
					self.c = True
				return (True,self.verbes.pop(0))
		else:
			return (False,())

	def conjugaison(self, id, temp):
		if(temp == "présent"):
			sql_query = "SELECT je,tu,il,nous,vous,ils FROM présent WHERE id = ?"
			self.cursor.execute(sql_query, (id,))
			conjug = self.cursor.fetchone()
			for i in range(6):
				aux = conjug[i]
				réponse = input(self.pronoms[i]+": ")
				if(réponse != aux):
					print("Désolé, vous avez erré. Vous avez doit typer -->",aux)
					self.add_Erreur(id, "présent")
					return False

		elif(temp == "passé composé"):
			sql_query = "SELECT auxiliaire, participe FROM Passé WHERE id = ?"
			self.cursor.execute(sql_query, (id,))
			conjug = self.cursor.fetchone()
			aux = input("Auxiliaire:")
			passé = input("Participe passé:")
			if(aux == conjug[0] and passé == conjug[1]):
				return True
			else:
				print("Desolé vous avez erré. Vous avez doit typer -->" , conjug[1])
				self.add_Erreur(id, "passé composé")
				return False

		elif(temp == "imparfait"):
			sql_query = "SELECT je,tu,il,nous,vous,ils FROM Imparfait WHERE id = ?"
			self.cursor.execute(sql_query, (id,))
			conjug = self.cursor.fetchone()
			for i in range(6):
				aux = conjug[i]
				réponse = input(self.pronoms[i]+": ")
				if(réponse != aux):
					print("Désolé, vous avez erré. Vous avez doit typer -->",aux)
					self.add_Erreur(id, "imparfait")
					return False

		elif(temp == "futur"):
			sql_query = "SELECT je,tu,il,nous,vous,ils FROM Futur WHERE id = ?"
			self.cursor.execute(sql_query, (id,))
			conjug = self.cursor.fetchone()
			for i in range(6):
				aux = conjug[i]
				réponse = input(self.pronoms[i]+": ")
				if(réponse != aux):
					print("Désolé, vous avez erré. Vous avez doit typer -->",aux)
					self.add_Erreur(id, "futur")
					return False
				
		elif(temp == "subjonctif"):
			sql_query = "SELECT je,tu,il,nous,vous,ils FROM Subjonctif WHERE id = ?"
			self.cursor.execute(sql_query, (id,))
			conjug = self.cursor.fetchone()
			
			for i in range(6):
				aux = conjug[i]
				réponse = input(self.pronoms[i]+": ")
				if(réponse != aux):
					print("Désolé, vous avez erré. Vous avez doit typer -->",aux)
					self.add_Erreur(id, "subjonctif")
					return False
		return True

	def add_Erreur(self, id, temp):
		sql_query = "SELECT * FROM Erreurs WHERE id = ?"
		self.cursor.execute(sql_query, (id,))
		l = self.cursor.fetchone()
		if(l == None):
			if(temp == "présent"):
				sql_query = "INSERT INTO Erreurs VALUES (?,1,0,0,0)"
				self.cursor.execute(sql_query, (id,))

			elif(temp == "passé composé"):
				sql_query = "INSERT INTO Erreurs VALUES (?,0,1,0,0)"
				self.cursor.execute(sql_query, (id,))

			elif(temp == "imparfait"):
				sql_query = "INSERT INTO Erreurs VALUES (?,0,0,1,0)"
				self.cursor.execute(sql_query, (id,))

			elif(temp == "futur"):
				sql_query = "INSERT INTO Erreurs VALUES (?,0,0,0,1)"
				self.cursor.execute(sql_query, (id,))

		else:
			if(temp == "présent"):
				l = (l[0], l[1]+1, l[2], l[3], l[4], l[5])
				sql_query = "UPDATE Erreurs SET present = ? WHERE id = ?"
				self.cursor.execute(sql_query, (l[1],id))

			elif(temp == "passé composé"):
				l = (l[0], l[1], l[2]+1, l[3], l[4], l[5])
				sql_query = "UPDATE Erreurs SET passe = ? WHERE id = ?"
				self.cursor.execute(sql_query, (l[2],id))

			elif(temp == "imparfait"):
				l = (l[0], l[1], l[2], l[3]+1, l[4], l[5])
				sql_query = "UPDATE Erreurs SET imparfait = ? WHERE id = ?"
				self.cursor.execute(sql_query, (l[3],id))

			elif(temp == "futur"):
				l = (l[0], l[1], l[2], l[3], l[4]+1, l[5])
				sql_query = "UPDATE Erreurs SET futur = ? WHERE id = ?"
				self.cursor.execute(sql_query, (l[4],id))
			
			elif(temp == "subjonctif"):
				l = (l[0], l[1], l[2], l[3], l[4], l[5]+1)
				sql_query = "UPDATE Erreurs SET subjonctif = ? WHERE id = ?"
				self.cursor.execute(sql_query, (l[5],id))

		print("l:",l)
		self.conn.commit()

	def addScore(self, user, temp, sc):
		sql_query = 'SELECT * FROM Users WHERE login = ?'
		if(temp == 'présent'):
			sql_query2 = 'UPDATE Users SET scorePre = ? WHERE login = ?'
			i = 4

		elif(temp == 'passé composé'):
			sql_query2 = 'UPDATE Users SET scorePass = ? WHERE login = ?'
			i = 5

		elif(temp == 'imparfait'):
			sql_query2 = 'UPDATE Users SET scoreImp = ? WHERE login = ?'
			i = 6

		elif(temp == 'futur'):
			sql_query2 = 'UPDATE Users SET scoreFutur = ? WHERE login = ?'
			i = 7

		elif(temp == 'subjonctif'):
			sql_query2 = 'UPDATE Users SET scoreSubj = ? WHERE login = ?'
			i = 7
		self.cursor.execute(sql_query, (user,))
		l = self.cursor.fetchone()
		if(sc > l[i]):
			self.cursor.execute(sql_query2, (sc,user))
		self.conn.commit()

	def futur(self):
		os.system("./get_futur.sh")
		input("pret?")

	def moitienne(self):
		table = []
		for row in self.cursor.execute("SELECT * FROM Erreurs"):
			row = (row[0],int(row[1]/2), int(row[2]/2), int(row[3]/2), int(row[4]/2), int(row[5]/2))
			table.append(row)

		#print(table)
		for element in table:
			self.cursor.execute("UPDATE Erreurs SET present = ?, passe = ?, imparfait = ?, futur = ?, subjonctif = ? WHERE id = ?", (element[1],element[2],element[3],element[4],element[5], element[0]))
		input('pret?')
		self.conn.commit()

	def close(self):
		self.conn.close()

		