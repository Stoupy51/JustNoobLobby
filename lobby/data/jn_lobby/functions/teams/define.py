
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
		teams (list): Liste des équipes sous la forme d'un tuple (nom, couleur, nb_joueurs, vanilla_color)

	Returns:
		None
	"""
	# Création du fichier
	f = open("create_teams.mcfunction", "w")
	f.write("\n")
	f.write("## Création des équipes\n")
	f.write("\n")

	# Création des équipes
	for nom, couleur, nb_joueurs, vanilla_color in teams:
		for i in range(nb_joueurs):

			# Indicatif de position
			col = couleur
			pos = "th"
			if i == 0:
				pos, col = "st", "#EBD759"
			elif i == 1:
				pos, col = "nd", "#C0C0C0"
			elif i == 2:
				pos, col = "rd", "#CD7F32"
			nbPos = str(i + 1)
			if len(nbPos) == 1:
				nbPos = "0" + nbPos

			# Création de l'équipe
			f.write(f'team add {nom}_{nbPos}\n')
			f.write(f'team modify {nom}_{nbPos} displayName {{"text":"{nom} - {i+1}{pos}","color":"{col}"}}\n')
			f.write(f'team modify {nom}_{nbPos} suffix {{"text":" [{nom} - {i+1}{pos}]","color":"{col}"}}\n')
			f.write(f'team modify {nom}_{nbPos} color {vanilla_color}\n')
			f.write("\n")
		
		# Création d'une équipe "???" pour placement inconnu
		f.write(f'team add {nom}_x\n')
		f.write(f'team modify {nom}_x displayName {{"text":"{nom} - ???","color":"{couleur}"}}\n')
		f.write(f'team modify {nom}_x suffix {{"text":" [{nom} - ???]","color":"{couleur}"}}\n')
		f.write(f'team modify {nom}_x color {vanilla_color}\n')
		f.write("\n")
	
	# Ajout de l'équipe "aMJ"
	f.write(f'team add MJ\n')
	f.write(f'team modify MJ displayName {{"text":"MJ","color":"dark_aqua"}}\n')
	f.write(f'team modify MJ suffix {{"text":" [MJ]","color":"dark_aqua"}}\n')
	f.write(f'team modify MJ color aqua\n')

	# Fermeture du fichier
	f.close()

# Définition des équipes
teams = [
	("S01", "#FA67FB", 18, "light_purple"),
	("S02", "#fd7839", 20, "gold"),
	("S03", "#5ee9f1", 18, "aqua"),
	("S04", "#209e26", 18, "dark_green"),
	("S05", "#f9e024", 21, "yellow"),
	("S06", "#fa2f2f", 18, "dark_red"),
	("S07", "#be6eee", 20, "dark_purple"),
	("S08", "#4ef158", 18, "green"),
	("S09", "#57c7c7", 18, "dark_aqua"),
	("S10", "#ff6868", 18, "red"),
	("S11", "#ee24a4", 21, "light_purple"),
	("S12", "#0240d1", 18, "dark_blue"),
]
create_teams_file(teams)




