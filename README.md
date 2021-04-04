# SpyroxasTimer

# Spyroxas-Timer

**Timer personnalisable pour une utilisation rapide pour les streams Twitch**

Laisse-moi t'expliquer comment fonctionne ce timer :

1 - Dans le fichier de "config.txt", il y a 4 paramètres que tu dois configurer:

	1 - le nombre de seconde d'attente
	
	2 - ton texte avant la dernière minute
	
	3 - ton texte pour la dernière minute
	
	4 - ton texte une fois le timer fini

*****************
**Remarques :**

Pour rendre ton texte interactif avec le timer, il existe des commandes que tu peux ajouter dans les différents textes :

{timer} => ajoute le temps restant sous le format MM:SS

{min} => ajoute le temps restant sous le format MM

{sec} => ajoute le temps restant sous le format SS

{plural_min} => ajoute un "s" s'il y a plusieurs minutes

{plural_sec} => ajoute un "s" s'il y a plusieurs secondes
*****************

2 - Sur ton logiciel de stream (Streamlabs OBS, OBS studio....) configure un lien entre un texte et le fichier "output.txt"

3 - Configure un de tes boutons (StreamDeck ou clavier avec touche macro) avec le logiciel stream Deck allez dans "Système" -> "Ouvrir" et sélectionnez le fichier "main.exe"
