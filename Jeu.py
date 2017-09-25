import Enumeration as E
import Banque_de_données as BD
import os

class Jeu(object):
	"""docstring for Jeu"""
	def __init__(self):
		self.bd = BD.Banque_de_données()
		self.diff = E.Difficulté.facile

	def main(self):
		print("hello")

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

	def login(self):
		usr = input("Utilisateur:")
		psw = input("Mot de passe:")
		(bol, name) = self.bd.login(usr, psw)
		return (bol,name)

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
			os.system("clear")
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
			
			os.system("clear")
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
		print("\t-----------------------------\n")

	def end(self):
		self.bd.close()