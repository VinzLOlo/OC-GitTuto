#!/usr/local/bin/python3.4
# -*- coding: utf-8 -*-

import os
from fonctions import *

os.chdir("/Users/Poussin/Documents/DevPyhton/OC_Pendu")


ligne = "***********************************"
print(ligne,"\n",ligne,"\n","--- Bienvenu au jeu du pendu !!! ---","\n",ligne,"\n",ligne)

#Algorithme
#Demander le nom du joueur (liste des noms déjà enregistrées ou nouveau nom)
#Afficher le score en cours
#Lancer une nouvelle partie ou quitter

# Déclaration des variables
FinPartie = False

# Programme Principal
while FinPartie == False: #Tant que False la partie continue	
	nom_test = input("Entrez votre nom :")

	#Test entrée utilisateur 
	if nom_test == "": 			#Vérification qu'un nom soit bien rentré
		print("Vous n'avez pas rentré de nom !!!")
		FinPartie = True

	else:
		#Chercher dans le fichier donnees si le nom existe
		#Si existe "Bonjour [Prénom] !!!, votre score actuel est [score]. Bonne chance"

		score = lecture_score() #Lecture des scores dans le fichier
		
		try:	
			print("Bonjour",nom_test,", votre score actuel est de", score[nom_test],"points. Bonne chance !")
			
		except:
			score[nom_test] = 0
			ecritute_score(score)	#Enregistrement du nouveau joueur
			print("Vous étes un nouveau joueur !")
			pass


		print("\n","Que la partie commence !!!","\n")


		
		


		FinPartie = True



	#Fonction de test de nom lecture dans fichier donnees
	#Si present afficher le score actuel
	#Si non demander la creation