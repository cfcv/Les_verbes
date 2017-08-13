class Jeu(object):
	"""docstring for Jeu"""
	def __init__(self):
		#self.bd = Banque_de_données()
		pass
	def main(self):
		print("hello")

	def présentation(self):
		print("\n\t\tLES VERBES\n")
	
	def menu(self):
		print("\t-----------------------------")
		print("\t1 - Indentifiez vous")
		print("\t2 - Créer votre compt")
		print("\t3 - Changer la difficulté")
		print("\t3 - Aider")
		print("\t4 - Sortir")
		print("\t5 - Options avancées")
		print("\t-----------------------------\n")


#-----------------------------
#MAIN
game = Jeu()
game.présentation()
game.menu()
choice = 0
while(choice == 0):
	choice = int(input("Choix:"))
	if(choice == 1):
		pass
	elif(choice == 2):
		pass
	elif(choice == 3):
		pass
	elif(choice == 4):
		pass
	elif(choice == 5):
		pass
	elif(choice == 6):
		pass
	else:
		print("Choisez un numéro entre 1-5")
		choice = 0	
#-----------------------------