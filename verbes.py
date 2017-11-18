import Jeu
import os
#-----------------------------
#MAIN
game = Jeu.Jeu()
game.présentation()
game.menu()
choice = 0
while(choice == 0):
	choice = int(input("Choix:"))

	#Indentifiez vous
	if(choice == 1):
		c,n,sp,spss,sim,sf,usr,data = game.login()
		if(not c):
			choice = 0
			print("utilisateur ou mot de passe erroné.")
		else:
			os.system("clear")
			print("Bienvenu ",n)
			print("Last active:",data)
			print("Maximum Score, Présent:",sp,"Passé composé:",spss,"Imparfait:",sim,"Futur",sf,"\n")
			game.main(usr)

			os.system("clear")
			game.présentation()
			game.menu()
			choice = 0

	#Créer votre compt
	elif(choice == 2):
		game.create_user()
		choice = 0

	#difficuĺté
	elif(choice == 3):
		pass

	#Aider
	elif(choice == 4):
		pass

	#Sortir
	elif(choice == 5):
		game.end()

	#Options avancées
	elif(choice == 6):
		choice = 0
		if(game.opt_avanc()):
			game.présentation()
			game.menu()
	
	else:
		print("Choisez un numéro entre 1-5")
		choice = 0	
#-----------------------------