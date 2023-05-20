
# Define.py : Ce script génère les fichiers .mcfunction pour les équipes
# ainsi que pour les joueurs qui appartiennent à une équipe

# Vérification de l'emplacement du script
import os
if os.getcwd() != os.path.dirname(os.path.realpath(__file__)):
	print("Please execute this script in the same folder as the script")
	exit()

# Définition des fonctions
def create_teams_file(teams: list):
	""" Créer le fichier .mcfunction pour les équipes
	Args:
		teams (list): Liste des équipes sous la forme d'un tuple (nom, couleur, nb_joueurs)

	Returns:
		None
	"""
	# Création du fichier
	f = open("create_teams.mcfunction", "w")
	f.write("\n")
	f.write("## Création des équipes\n")
	f.write("\n")

	# Création des équipes
	for nom, couleur, nb_joueurs in teams:
		for i in range(nb_joueurs):

			# Indicatif de position
			col = couleur
			pos = "th"
			if i == 0:
				pos, col = "st", "#FFE700"
			elif i == 1:
				pos, col = "nd", "#C0C0C0"
			elif i == 2:
				pos, col = "rd", "#CD7F32"

			# Création de l'équipe
			f.write(f'team add {nom}_{i+1}\n')
			f.write(f'team modify {nom}_{i+1} displayName {{"text":"{nom} - {i+1}{pos}","color":"{col}"}}\n')
			f.write(f'team modify {nom}_{i+1} suffix {{"text":"[{nom} - {i+1}{pos}]","color":"{col}"}}\n')
			f.write("\n")
		
		# Création d'une équipe "???" pour placement inconnu
		f.write(f'team add {nom}_x\n')
		f.write(f'team modify {nom}_x displayName {{"text":"{nom} - ???","color":"{couleur}"}}\n')
		f.write(f'team modify {nom}_x suffix {{"text":"[{nom} - ???]","color":"{couleur}"}}\n')

	# Fermeture du fichier
	f.close()

# Définition des équipes
teams = [
	("S01", "#FA67FB", 18),
	("S02", "#fd7839", 20),
	("S03", "#5ee9f1", 18),
	("S04", "#209e26", 18),
	("S05", "#f9e024", 21),
	("S06", "#fa2f2f", 18),
	("S07", "#be6eee", 20),
	("S08", "#4ef158", 18),
	("S09", "#57c7c7", 18),
	("S10", "#ff6868", 18),
	("S11", "#ee24a4", 21),
	("S12", "#0240d1", 18)
]
create_teams_file(teams)




