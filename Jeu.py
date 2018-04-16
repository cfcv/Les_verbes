import Enumeration as E
import Banque_de_données as BD
import os

class Jeu(object):
	"""docstring for Jeu"""
	def __init__(self):
		self.bd = BD.Banque_de_données()
		self.diff = E.Difficulté.facile
		self.tupla = tuple()
		self.possibilités = list(["présent","passé composé", "imparfait", "futur", "subjonctif"])

	def login(self):
		usr = input("Utilisateur:")
		psw = input("Mot de passe:")
		(bol, name, sp, spss, sim, sf, ssubj, user,data) = self.bd.login(usr, psw)
		return (bol, name, sp, spss, sim, sf, ssubj, user,data)

	def main(self, user):
		print("Quel temp verbal vous souhaitez pratiquer?")
		print("possibilités:",self.possibilités)
		r = input("Réponse:")
		
		self.score = 0
		if(r in self.possibilités):
			self.bd.inicializa_words(r)
			b = True
			while(b):
				b, self.tupla = self.bd.random_word()
				if(b):
					print("Score:",self.score)
					print("("+self.tupla[2]+") Conjuguez le verbe suivant au", r+ ":",self.tupla[1])
					b = self.bd.conjugaison(self.tupla[0], r)
					if(b):
						os.system("cls")
						self.score += 1
					else:
						self.print_score()
						self.bd.addScore(user, r, self.score)
						input("Essayez à nouveau!")

				else:
					print("Felicitations!!! vous êtes un ninja en",r)
					self.bd.addScore(user,r,self.score)
					input('Súper!')

		else:
			print("Vous devez choisir un temp verbel valide")
			input("D'accord?")
		return

	def présentation(self):
		print("\n\t\tLES VERBES\n")

	def create_user(self):
		prenom = input("Votre prenom:")
		usr = input("Votre utilisateur:")
		psw1 = input("Mot de passe:")
		psw2 = input("Repetez votre mot de passe:")
		if(psw1 == psw2):
			print(prenom," ",usr," ",psw1)
			c = input("Vous êtes sûr?[oui/non]:")
			if(c == "oui"):
				self.bd.creer_compt(prenom, usr, psw1)
		else:
			print("Les mots de passe doivent être les mêmes.")


	def menu(self):
		print("\t-----------------------------")
		print("\t1 - Indentifiez vous")
		print("\t2 - Créer votre compt")
		print("\t3 - Changer la difficulté(Facile par défaut)")
		print("\t4 - Aider")
		print("\t5 - Sortir")
		print("\t6 - Options avancées")
		print("\t-----------------------------\n")

	def opt_avanc(self):
		psw = input("Mot de passe:")
		if(psw == "1234"):
			os.system("cls")
			print("\n\t\tZONE RÉSERVÉE\n")
			self.print_avanc()
			
			c = int(input("Choix:"))
			#lister utilisateurs
			if(c == 1):
				self.bd.lister_utilisateurs()

			#lister verbes
			elif(c == 2):
				self.bd.lister_verbes()	

			#Ajouter un verbe
			elif(c == 3):
				self.bd.Ajouter_verbe()
				
			#Ajouter conjugaison
			elif(c == 4):
				self.bd.Ajouter_conjugaison()

			#Lister tables	
			elif(c == 5):
				self.bd.lister_table()

			#Accioner le script
			elif(c == 6):
				self.bd.futur()
			
			#moitienne
			elif(c == 7):
				self.bd.inicializa_score()
				self.bd.moitienne()

			os.system("cls")
			return True
		
		else:
			print("Erreur")
			return False

	def print_avanc(self):
		print("\t-----------------------------")
		print("\t1 - Lister utilisateurs")
		print("\t2 - Lister les verbes")
		print("\t3 - Ajouter un verbe")
		print("\t4 - Ajouter conjugaison")
		print("\t5 - Lister tables")
		print("\t6 - Script")
		print("\t7 - moitienne")
		print("\t-----------------------------\n")

	def print_score(self):
		if(self.score < 10):
			print("\n\n\t\t*********")
			print("\t\t"+"*  ",self.score,"  *")
			print("\t\t*********")
			
		else:
			print("\n\n\t\t**********")
			print("\t\t"+"*  ",self.score,"  *")
			print("\t\t**********")

		print("\n\n")

	def end(self):
		self.bd.close()