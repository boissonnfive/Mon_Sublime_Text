# Raccourcis Sublime Text

## Fichiers ##

- ctrl+o        / super+o       : ouvrir un fichier
- ctrl+w        / super+w       : fermer un fichier
- ctrl+s        / super+s       : enregistrer un fichier
- ctrl+shift+s  / super+shift+s : enregistrer un fichier sous un autre nom
- super+shift+t / ctrl+shift+t  : Réouvrir le dernier fichier fermé (cyclique)


## Edition ##

- Majuscule               : ctrl+k+u
- Minuscule               : ctrl+k+l
- Première lettre en maj. : ctrl+k+t  / super+k+t
- Aller à la ligne        : ctrl+entrée
- Indenter                : ctrl+)
- Désindenter             : ctrl+^
- Commenter               : ctrl+/    (pas de shift)
- Commenter une sélection : ctrl+shift+/
- Plier tout              : ctrl+k+1 ou ctrl+&    / super+k+1
- Déplier tout            : ctrl+k+0 ou ctrl+k+j  / super+k+0
- Console                 : ctrl+ù

*NOTES:*

- Si on met :{ "keys": ["ctrl+k", "ctrl+t"], "command": "title_case" } dans ses préférences utilisateur
- Pour le pliage du code, on peut utiliser les petits triangles dans la marge.


### Multiple Line Edition ###

For example, to make the same edit on multiple lines, split the selection into lines (Ctrl+Shift+L on Windows and Linux, Command+Shift+L on OS X), and start navigating the cursors and type. Your actions will occur simultaneously at each cursor.


## Sélection ##

- Sélection verticale         : shift+clic droit souris / alt+ clic gauche souris
- Sélection de la portée (*)  : ctrl+shift+espace      / super+shift+espace
- Parenthèse/crochet/accolade : ctrl+m                 / ctrl+m
- Sélection de l'indentation  : ctrl+shift+j           / super+shift+j

(*) : très utile pour les parenthèses, les crochets, les balises HTML, etc ...

### Modifier toutes les variables en même temps ###

1. Sélectionner la variable.
2. Taper «Alt + F3» ou «ctrl+super+g».
3. Modifier toutes les occurences de la variable en même temps.

ou

To rename a variable within a function, position the cursor next to it, and press Select More (Ctrl+D on Windows and Linux, Command+D on OS X) several times to select all occurrences, and then start typing to rename them all. 
Quick Skip Next (Ctrl+K, Ctrl+D), to skip over matches, so you can select just the ones you want.


## Rechercher/Remplacer ##

- Rechercher                   : ctrl+f       / super+f
- Remplacer                    : ctrl+h       / super+h
- Rechercher dans des fichiers : shift+ctrl+f / super+shift+f
- Suivant                      : F3           / super+g
- Précédent                    : shift+F3     / super+shift+g
- Recherche incrémentale (*)   : ctrl+i       / super+i

(*) : répeter le raccourci pour rechercher le suivant (ajouter shift pour le précédent).


## Manipulation des fenêtres/écrans/onglets ##

- Nouvelle fenêtre         : ctrl+shift+n
- Fermer une fenêtre       : ctrl+shift+w
- Diviser l'écran en 2     : shift+alt+2  / super+alt+2
- Revenir à un seul écran  : shift+alt+1  / super+alt+1
- Diviser l'écran en 4     : shift+alt+5  / super+alt+5
- Déplacer dans l'écran X  : ctrl+shift+X / ctrl+shift+X 
- Aller dans l'écran X     : ctrl+X       / ctrl+X
- changer d'onglet         : ctrl+tab     / ctrl+tab
- fermer un onglet         : ctrl+w       / super+w
