
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

	# Fermeture du fichier et retour
	f.write("\n")
	f.close()
	return None


def create_players_file(players: list) -> None:
	""" Créer le fichier .mcfunction pour les joueurs
	Args:
		players (list): Liste des joueurs sous la forme d'une liste [pseudo, saison string, position string]

	Returns:
		None
	"""
	# Création du fichier
	f = open("create_players.mcfunction", "w")
	f.write("\n")
	f.write("## Mise en team des joueurs\n")
	f.write("\n")

	# Création des joueurs
	for l in players:

		# Skip si la ligne est vide
		if l == [""]:
			continue

		# Récupération des données
		pseudo = l[0]
		saison = l[1].split(" - ")[0]
		pos = "x"
		if (l[2] != ""):
			pos = l[2].split("/")[0]

		# Création de la ligne qui met le joueur dans l'équipe
		f.write(f'team join {saison}_{pos} {pseudo}\n')

	# Join des joueurs sans équipe dans l'équipe "new"
	f.write(f'team join new @a[team=]\n')

	# Fermeture du fichier et retour
	f.write("\n")
	f.close()
	return None



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

# Définition des joueurs
players = """
Akariaa	S01 - Lonely Island 🏝️	01/18
Kxala_a	S01 - Lonely Island 🏝️	02/18
SteelPikachuuu	S01 - Lonely Island 🏝️	03/18
DontBeAKidVinz	S01 - Lonely Island 🏝️	04/18
DontBeAKidVinz	S11 - Ecera: Second Chance 💃	19/21
Judipie	S01 - Lonely Island 🏝️	05/18
Axaltau	S01 - Lonely Island 🏝️	06/18
EdenMan	S01 - Lonely Island 🏝️	07/18
EdenMan	S11 - Ecera: Second Chance 💃	
Pomkazz	S01 - Lonely Island 🏝️	08/18
Maxator34_	S01 - Lonely Island 🏝️	09/18
Srangee	S01 - Lonely Island 🏝️	10/18
Srangee	S11 - Ecera: Second Chance 💃	
Dari76	S01 - Lonely Island 🏝️	11/18
LePetitChacou	S01 - Lonely Island 🏝️	12/18
LePetitChacou	S07 - Ichoria: Second Chance 🎆	11/20
Pepitot	S01 - Lonely Island 🏝️	13/18
Pepitot	S07 - Ichoria: Second Chance 🎆	07/20
cozotidg	S01 - Lonely Island 🏝️	14/18
cozotidg	S07 - Ichoria: Second Chance 🎆	15/20
DontBeAKidClem	S01 - Lonely Island 🏝️	15/18
Bafalo	S01 - Lonely Island 🏝️	16/18
PikIronMan	S01 - Lonely Island 🏝️	17/18
PikIronMan	S07 - Ichoria: Second Chance 🎆	13/20
Comte_L	S01 - Lonely Island 🏝️	18/18
TomSawyerWolf	S02 - Harun ❄️	01/20
TheRedMan88	S02 - Harun ❄️	02/20
ElSanjo	S02 - Harun ❄️	03/20
Elzariia	S02 - Harun ❄️	04/20
Mr2Exil5D	S02 - Harun ❄️	05/20
Mr2Exil5D	S11 - Ecera: Second Chance 💃	
scartvol	S02 - Harun ❄️	06/20
P0cky_0	S02 - Harun ❄️	07/20
P0cky_0	S11 - Ecera: Second Chance 💃	
AdraiK	S02 - Harun ❄️	08/20
Arlovie_	S02 - Harun ❄️	09/20
Arlovie_	S11 - Ecera: Second Chance 💃	21/21
Valtintino	S02 - Harun ❄️	10/20
Ragiel_	S02 - Harun ❄️	11/20
Rafloppa	S02 - Harun ❄️	12/20
Rafloppa	S07 - Ichoria: Second Chance 🎆	05/20
Xenooh	S02 - Harun ❄️	13/20
Saiito	S02 - Harun ❄️	14/20
Ruster_	S02 - Harun ❄️	15/20
Fusoya_	S02 - Harun ❄️	16/20
Lumeteros	S02 - Harun ❄️	17/20
LinkStart_	S02 - Harun ❄️	18/20
Viken78	S02 - Harun ❄️	19/20
Viken78	S07 - Ichoria: Second Chance 🎆	09/20
MKeh	S02 - Harun ❄️	20/20
Ydrolics	S03 - Floating Islands 🐦	01/18
arcanial	S03 - Floating Islands 🐦	02/18
Noereau	S03 - Floating Islands 🐦	03/18
Islijelis	S03 - Floating Islands 🐦	04/18
zCurl	S03 - Floating Islands 🐦	05/18
DontBeAKidMath	S03 - Floating Islands 🐦	06/18
DeadRed	S03 - Floating Islands 🐦	07/18
Gnagna_	S03 - Floating Islands 🐦	08/18
Gnagna_	S11 - Ecera: Second Chance 💃	20/21
Antho60	S03 - Floating Islands 🐦	09/18
Antho60	S11 - Ecera: Second Chance 💃	14/21
Redemoles	S03 - Floating Islands 🐦	10/18
DontBeAKidAnna	S03 - Floating Islands 🐦	11/18
DontBeAKidAnna	S11 - Ecera: Second Chance 💃	
Shazin	S03 - Floating Islands 🐦	12/18
Shazin	S07 - Ichoria: Second Chance 🎆	04/20
Unicorn_Zoe	S03 - Floating Islands 🐦	13/18
Unicorn_Zoe	S07 - Ichoria: Second Chance 🎆	18/20
Pouka	S03 - Floating Islands 🐦	14/18
SimonzeMK	S03 - Floating Islands 🐦	15/18
EvoRay	S03 - Floating Islands 🐦	16/18
EvoRay	S07 - Ichoria: Second Chance 🎆	19/20
Aleksai_i	S03 - Floating Islands 🐦	17/18
Waniis	S03 - Floating Islands 🐦	18/18
MrCT_	S04 - Champions v Contenders 🏆	01/18
Narva_	S04 - Champions v Contenders 🏆	02/18
Lidqil	S04 - Champions v Contenders 🏆	03/18
San_Mononoke	S04 - Champions v Contenders 🏆	04/18
kit_cat04	S04 - Champions v Contenders 🏆	05/18
FayeurMonkey	S04 - Champions v Contenders 🏆	06/18
FayeurMonkey	S11 - Ecera: Second Chance 💃	17/21
Oraclette	S04 - Champions v Contenders 🏆	07/18
Hiruko_Senpai	S04 - Champions v Contenders 🏆	08/18
Feynoox_	S04 - Champions v Contenders 🏆	09/18
Feynoox_	S11 - Ecera: Second Chance 💃	18/21
ArtiGrrr	S04 - Champions v Contenders 🏆	10/18
ArtiGrrr	S11 - Ecera: Second Chance 💃	
KaiiGoat	S04 - Champions v Contenders 🏆	11/18
Floflolino	S04 - Champions v Contenders 🏆	12/18
Floflolino	S07 - Ichoria: Second Chance 🎆	14/20
_Megabyte	S04 - Champions v Contenders 🏆	13/18
_Megabyte	S07 - Ichoria: Second Chance 🎆	06/20
DontBeAKidLuca	S04 - Champions v Contenders 🏆	14/18
DontBeAKidLuca	S07 - Ichoria: Second Chance 🎆	12/20
_Paulo_	S04 - Champions v Contenders 🏆	15/18
Skylaa	S04 - Champions v Contenders 🏆	16/18
Mathzalli	S04 - Champions v Contenders 🏆	17/18
Mathzalli	S07 - Ichoria: Second Chance 🎆	17/20
DontBeAKidErwan	S04 - Champions v Contenders 🏆	18/18
Nintasma	S05 - Lios 🍃	01/21
ItsIno_	S05 - Lios 🍃	02/21
Sagnosis	S05 - Lios 🍃	02/21
Eca_	S05 - Lios 🍃	04/21
Katar0s	S05 - Lios 🍃	05/21
Katar0s	S11 - Ecera: Second Chance 💃	13/21
Stoupy51	S05 - Lios 🍃	06/21
TheHernest	S05 - Lios 🍃	07/21
Maxow	S05 - Lios 🍃	08/21
TheMisteryHugo	S05 - Lios 🍃	09/21
TheMisteryHugo	S11 - Ecera: Second Chance 💃	
Silkyy__	S05 - Lios 🍃	10/21
Antoineuuh	S05 - Lios 🍃	11/21
Antoineuuh	S11 - Ecera: Second Chance 💃	15/21
Totay_	S05 - Lios 🍃	12/21
Totay_	S07 - Ichoria: Second Chance 🎆	01/20
0ri0n03	S05 - Lios 🍃	13/21
0ri0n03	S07 - Ichoria: Second Chance 🎆	20/20
Lawef	S05 - Lios 🍃	14/21
Lawef	S07 - Ichoria: Second Chance 🎆	16/20
GhostRom	S05 - Lios 🍃	15/21
SuperChouette666	S05 - Lios 🍃	16/21
_Miilky	S05 - Lios 🍃	17/21
Luxysia	S05 - Lios 🍃	18/21
DarkGiant24	S05 - Lios 🍃	19/21
DarkGiant24	S07 - Ichoria: Second Chance 🎆	02/20
_Diso	S05 - Lios 🍃	20/21
_Diso	S07 - Ichoria: Second Chance 🎆	02/20
Lazar__	S05 - Lios 🍃	21/21
Grenzo_67	S06 - Tropical Gardens 🎍	01/18
JxyL	S06 - Tropical Gardens 🎍	02/18
Palishka	S06 - Tropical Gardens 🎍	02/18
DontBeAKidKelvin	S06 - Tropical Gardens 🎍	04/18
_Alienor	S06 - Tropical Gardens 🎍	05/18
DontBeAKidMathis	S06 - Tropical Gardens 🎍	06/18
DontBeAKidMathis	S11 - Ecera: Second Chance 💃	
weer94	S06 - Tropical Gardens 🎍	07/18
weer94	S11 - Ecera: Second Chance 💃	16/21
RhafyRicch	S06 - Tropical Gardens 🎍	08/18
Phylalix	S06 - Tropical Gardens 🎍	09/18
BerenGaldos	S06 - Tropical Gardens 🎍	10/18
BerenGaldos	S11 - Ecera: Second Chance 💃	
Filouche	S06 - Tropical Gardens 🎍	11/18
Malthus_	S06 - Tropical Gardens 🎍	12/18
OffSiab	S06 - Tropical Gardens 🎍	13/18
Pirananass	S06 - Tropical Gardens 🎍	14/18
Pirananass	S07 - Ichoria: Second Chance 🎆	10/20
CurtosTardos	S06 - Tropical Gardens 🎍	15/18
SilverF0x_	S06 - Tropical Gardens 🎍	16/18
Dark_Ail	S06 - Tropical Gardens 🎍	17/18
Dark_Ail	S07 - Ichoria: Second Chance 🎆	08/20
FloLeKebabier	S06 - Tropical Gardens 🎍	18/18
Thyxou	S08 - Aswaria 🚢	01/18
Lombosa	S08 - Aswaria 🚢	02/18
Sid_dy	S08 - Aswaria 🚢	03/18
Falmo_	S08 - Aswaria 🚢	04/18
Falmo_	S11 - Ecera: Second Chance 💃	
TreekoZ	S08 - Aswaria 🚢	05/18
TreekoZ	S11 - Ecera: Second Chance 💃	
LeGrandPigre	S08 - Aswaria 🚢	06/18
Bomby_	S08 - Aswaria 🚢	07/18
titou2000	S08 - Aswaria 🚢	08/18
Agents_S	S08 - Aswaria 🚢	09/18
Sean__n	S08 - Aswaria 🚢	10/18
Walda666	S08 - Aswaria 🚢	11/18
Nebuleuh	S08 - Aswaria 🚢	12/18
Nebuleuh	S11 - Ecera: Second Chance 💃	
Yoddle_Yoddle	S08 - Aswaria 🚢	13/18
LucLec0	S08 - Aswaria 🚢	14/18
Stormerz	S08 - Aswaria 🚢	15/18
BambiSot	S08 - Aswaria 🚢	16/18
_TwiiiX	S08 - Aswaria 🚢	17/18
Kuery_	S08 - Aswaria 🚢	18/18
Glowthon	S09 - Zhen Zhou 🌾	01/18
Marimiss	S09 - Zhen Zhou 🌾	02/18
MikoMan	S09 - Zhen Zhou 🌾	02/18
Will_Boss_Gamer	S09 - Zhen Zhou 🌾	04/18
M4TOUW	S09 - Zhen Zhou 🌾	05/18
Lenya__	S09 - Zhen Zhou 🌾	06/18
Owenou	S09 - Zhen Zhou 🌾	07/18
tgi74	S09 - Zhen Zhou 🌾	08/18
Traumatisant	S09 - Zhen Zhou 🌾	09/18
math730	S09 - Zhen Zhou 🌾	10/18
Nekoss__	S09 - Zhen Zhou 🌾	11/18
Thakeax	S09 - Zhen Zhou 🌾	12/18
JeanChristophe	S09 - Zhen Zhou 🌾	13/18
JulDragonne	S09 - Zhen Zhou 🌾	14/18
RomainLeRoux	S09 - Zhen Zhou 🌾	15/18
Loufocah	S09 - Zhen Zhou 🌾	16/18
3llipse	S09 - Zhen Zhou 🌾	17/18
Rodakk1	S09 - Zhen Zhou 🌾	18/18
Arobaze	S10 - Nazgarth 🌙	01/18
Sili	S10 - Nazgarth 🌙	02/18
Horend	S10 - Nazgarth 🌙	03/18
NavySim	S10 - Nazgarth 🌙	04/18
MatthieuClam	S10 - Nazgarth 🌙	05/18
Zita_Orangegirl	S10 - Nazgarth 🌙	06/18
Scan__	S10 - Nazgarth 🌙	07/18
Timocaf	S10 - Nazgarth 🌙	08/18
Canfav_	S10 - Nazgarth 🌙	09/18
Akwaden	S10 - Nazgarth 🌙	10/18
Minaato_	S10 - Nazgarth 🌙	11/18
G0ldX	S10 - Nazgarth 🌙	12/18
_Pegasus	S10 - Nazgarth 🌙	13/18
Winner2TORGVoice	S10 - Nazgarth 🌙	14/18
NekoOkayu	S10 - Nazgarth 🌙	15/18
Ajad_	S10 - Nazgarth 🌙	16/18
YassineJoestar	S10 - Nazgarth 🌙	17/18
SwiizyHD	S10 - Nazgarth 🌙	18/18
Maarcouscous	S12 - Chroma Eruption 🌈	
CestAntoine	S12 - Chroma Eruption 🌈	
ClementDD	S12 - Chroma Eruption 🌈	
ManuPourLesIntim	S12 - Chroma Eruption 🌈	
MaThYx33	S12 - Chroma Eruption 🌈	
Megamat_	S12 - Chroma Eruption 🌈	
myATOM27	S12 - Chroma Eruption 🌈	
Remelta	S12 - Chroma Eruption 🌈	
Rizio_	S12 - Chroma Eruption 🌈	
xNicely	S12 - Chroma Eruption 🌈	
Neyga	S12 - Chroma Eruption 🌈	
Lowhere	S12 - Chroma Eruption 🌈	12/18
Mr_calbdr	S12 - Chroma Eruption 🌈	13/18
YiazElsio	S12 - Chroma Eruption 🌈	14/18
pegafil	S12 - Chroma Eruption 🌈	15/18
Nanows	S12 - Chroma Eruption 🌈	16/18
ZMC_Yoann	S12 - Chroma Eruption 🌈	17/18
ShawDen_	S12 - Chroma Eruption 🌈	18/18
"""
# On split en liste [[pseudo, saison string, position string], ...]
players = players.split("\n")
newP = []
for p in players:
	newP.append(p.split("\t"))
players = newP
create_players_file(players)

