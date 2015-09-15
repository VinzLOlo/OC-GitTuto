#!/usr/local/bin/python3.4
# -*- coding: utf-8 -*-

import os
import pickle

def lecture_data(nom_test):
	with open("data.txt", "r") as fichier:
		print (fichier.read())

def ecriture_data():
	with open("data.txt", "a") as fichier:
		fichier.write("Test")

def ecritute_score(score):
	with open("scores", "wb") as fichier:
		mon_pickler = pickle.Pickler(fichier)
		mon_pickler.dump(score)

def lecture_score():
	try:
		with open("scores", "rb") as fichier:
			mon_depickler = pickle.Unpickler(fichier)
			score = mon_depickler.load()
		return score
	except EOFError:
		pass #Fihcier vide