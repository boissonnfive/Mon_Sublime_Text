# Raccourcis Sublime Text

*[Remarque : sauf exception, ctrl doit être remplacé par ⌘ sur mac et super sur linux]*

[ ⌘ ⏏ ↩︎ ⇥ ^ ⇪ ⇧ ⎋ ⌥ ⇞ ⇟ ↑ ↓ ← → ]

## Fichiers ##

- ouvrir un fichier                            : ctrl+o
- fermer un fichier                            : ctrl+w
- enregistrer un fichier                       : ctrl+s
- enregistrer un fichier sous un autre nom     : ctrl+shift+s
- Réouvrir le dernier fichier fermé (cyclique) : ctrl+shift+t


## Edition ##

- Majuscule               : ctrl+k+u
- Minuscule               : ctrl+k+l
- Première lettre en maj. : ctrl+k+t
- Aller à la ligne        : ctrl+entrée
- Indenter                : ctrl+)
- Désindenter             : ctrl+^
- Commenter               : ctrl+/    (pas de shift)
- Commenter une sélection : ctrl+shift+/
- Plier tout              : ctrl+k+1 ou ctrl+&
- Déplier tout            : ctrl+k+0 ou ctrl+k+j
- Console                 : ctrl+ù

*NOTES:*

- Si on met :{ "keys": ["ctrl+k", "ctrl+t"], "command": "title_case" } dans ses préférences utilisateur
- Pour le pliage du code, on peut utiliser les petits triangles dans la marge.


## Sélection ##

- Sélection verticale         : shift+clic droit       [alt+clic gauche]
- Sélection de la portée (*)  : ctrl+shift+espace
- Parenthèse/crochet/accolade : ctrl+m                 [ctrl+m]
- Sélection de l'indentation  : ctrl+shift+j
- Sélection en lignes         : ctrl+shift+l

(*) : très utile pour les parenthèses, les crochets, les balises HTML, etc ...

### Modifier toutes les variables en même temps ###

1. Sélectionner la variable.
2. Taper « alt+F3 » ou « ctrl+super+g ».
3. Modifier toutes les occurences de la variable en même temps.

ou

1. Sélectionner la variable.
2. Taper « ctrl+d » pour chaque occurence de la variable.
3. Taper « ctrl+k, ctrl+d » pour sauter une occurence.
4. Modifier toutes les occurences de la variable en même temps.


## Rechercher/Remplacer ##

- Rechercher                   : ctrl+f
- Remplacer                    : ctrl+h
- Rechercher dans des fichiers : ctrl+shift+f
- Suivant                      : F3                      [super+g]
- Précédent                    : shift+F3                [super+shift+g]
- Recherche incrémentale (*)   : ctrl+i

(*) : répeter le raccourci pour rechercher le suivant (ajouter shift pour le précédent).


## Manipulation des fenêtres/écrans/onglets ##

- Nouvelle fenêtre         : ctrl+shift+n
- Fermer une fenêtre       : ctrl+shift+w
- Diviser l'écran en 2     : shift+alt+2                 [super+alt+2]
- Revenir à un seul écran  : shift+alt+1                 [super+alt+1]
- Diviser l'écran en 4     : shift+alt+5                 [super+alt+5]
- Déplacer dans l'écran X  : ctrl+shift+X                [ctrl+shift+X]
- Aller dans l'écran X     : ctrl+X                      [ctrl+X]
- changer d'onglet         : ctrl+tab                    [ctrl+tab]
- fermer un onglet         : ctrl+w
