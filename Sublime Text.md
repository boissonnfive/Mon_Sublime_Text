# Sublime Text

## Présentation

C'est un éditeur que j'utilise pour écrire des notes (principalement en Markdown). Je voudrais bien le maîtriser aussi bien que TextMate avec lequel je sais bien coder en HTML/CSS/PHP.


## Les raccourcis que j'utilise

Pour obtenir les raccourcis sur mac, il faut remplacer Ctrl par ⌘, sauf quand il y a un astérisque (*) dans le raccourci. Dans les autres cas, le raccourci mac est écrit.

### Génériques ###

- Passer en majuscule                                       : ⌘ K U
- Passer en minuscule                                       : ⌘ K L
- Mettre la première lettre en majuscule                    : ⌘ K T [1](1)
- Sélectionner toutes les occurences d'une variable         : ⌘ ⌃ G
- Sélectionner une occurence de plus d'une variable         : ⌘ D
- Déplacer une ligne                                        : ⌘ ⌃ ↑ ou ↓
- Se ballader dans les onglets                              : Ctrl + ⇥
- Rechercher                                                : ⌘ F
- Remplacer                                                 : ⌥ ⌘ F
- Suivant                                                   : ⌘ G
- Rechercher dans des fichiers                              : ⌘ ⇧ F
- Afficher la palette de commandes                          : ⌘ ⇧ P
- Ré-ouvrir le dernier fichier fermé                        : ⌘ ⇧ T
- Aligner les : ou = dans une sélection de lignes           : ⌘ ⌃ A [2](2)
- Sélectionner plusieurs colonnes                           : ⇧ Clic droit (⌥ clic)
- Sélectionner X lignes pour avoir X curseurs               : ⌘ ⇧ L


### Programmation ###

- Aller à la ligne, quand on est au milieu de la ligne avec : ⌘  ↩
- Insérer un bout de code (snippet)                         : raccourci   ⇥
- Sélectionner la portée                                    : ⌥ ⇧ espace
- Sélectionner le contenu entre parenthèses ou crochets     : ⌃ ⇧ M
- Mettre en commentaires                                    : ⌘ ⇧ :
- [HTML] Entourer la sélection avec une balise HTML         : ⌃ ⇧ w
- [HTML] Sélectionner le contenu de la balise               : ⌘ ⇧ A
- Afficher le scope                                         : ⌃ ⇧ P
- Aller                                                     :
    + au fichier                                            : ⌘ P lettres fichier
    + à la fonction                                         : ⌘ P @ lettres fction
    + à la ligne                                            : ⌘ P @ n° ligne
- Sélectionner le langage                                   : ⌘ ⇧ P ss langage


### Markdown ###

- Augmenter le niveau d'un titre (MarkdownEditing)          : # sur sélection
- Mettre en gras                 (MarkdownEditing)          : ⌘ ⌥ B
- Mettre en italique             (MarkdownEditing)          : ⌘ ⌥ I
- Augmente/Diminue le niveau des titres   (SmartMarkdown)   : ⌘ ⇧ ; / ⌘ ⇧ ,
- Plier les titres               (SmartMarkdown)            : ⇥
- Afficher un aperçu HTML        (Markdown Preview)         : ⌥ M


[1] : si on met :{ "keys": ["ctrl+k", "ctrl+t"], "command": "title_case" } dans ses préférences utilisateur
[2] : nécessite le module *Alignment*
[3] : nécessite le module *SmartMarkdown*



## Les astuces

### Créer un projet

1. Mettre tous les fichiers de son projet dans un dossier
1. Ajouter ce dossier à votre projet (qui va ainsi être créé): **Project > Add Folder to Project…** (Les fichiers du dossier doivent maintenant apparaître dans la barre latérale)
1. Enregistrer le projet: **Project > Save Project As…**. 2 fichiers sont créés:

    your_project.sublime-project
    your_project.sublime-workspace

### Ouvrir un fichier en hexadécimal

1. Menu File > Reopen with Encoding
2. Hexadecimal


### Les dossiers de configuration

- Windows : %APPDATA%\Sublime Text 3
- OS X    : ~/Library/Application Support/Sublime Text 3
- Linux   : ~/.config/sublime-text-3


### Taper des commandes python

Aller dans la console (Ctrl+`) ou View -> Show Console et taper :

    sublime.version()

### C/C++

- ctrl+b       : compiler le fichier (créer un fichier .exe).
- ctrl+shift+b : lancer le fichier (la sortie est affichée dans Sublime Text)
- ctrl+)       : Indenter
- ctrl+^       : Désindenter


## Ma config

### Paquets installés

- **package control**  : pour installer de nouveaux paquets
- **MarkdownEditing**  : pour afficher les fichiers markdown + raccourcis
- **Markdown Preview** : pour afficher un fichier Markdown en HTML dans le navigateur (⌥ M)
    + Markdown Preview: Preview in Browser
    + Markdown Preview: Export HTML in Sublime Text
    + Markdown Preview: Copy to Clipboard
    + Markdown Preview: Open Markdown Cheat sheet
    + Permet d'utiliser son propre modèle HTML
- **SmartMarkdown**    : copie le fonctionnement de orgmode pour Markdown
    + Pliage/Dépliage des titres (⇥)
    + Pliage/Dépliage global (Maj + ⇥)
    + Augmente/Diminue le niveau des titres (⌘ ⇧ ; / ⌘ ⇧ ,)
    + Continuation des listes après appuis sur ↩
    + Tableaux intelligents (⇥)
- **VBSript**          : coloration syntaxique + snippets pour VBScript
- **Alignment**        : pour aligner le texte selon : ou =
- **FindKeyConflicts** : Recherche les raccourcis associés à plusieurs paquets
- **mdTODO**           :
- **orgmode**          : pour faire du orgmode dans Sublime Text

## Mes Modifications

### Complétion

source : <http://docs.sublimetext.info/en/latest/reference/completions.html>

(voir mon fichier Bruno.sublime-completions)

### Première lettre en majuscule ###

- but          : Créer un raccourci windows pour mettre en majuscule la première lettre du mot sous le curseur
- fichier      : Default (Windows).sublime-keymap
- localisation : "C:\Users\Bruno\AppData\Roaming\Sublime Text 2\Packages\User"
- modification :

        // Pour mettre en majuscule la première lettre du mot sous le curseur
        { "keys": ["ctrl+k", "ctrl+t"], "command": "title_case" },


- but          : Créer un raccourci OSX pour mettre en majuscule la première lettre du mot sous le curseur
- fichier      : Default (OSX).sublime-keymap
- localisation : "/Users/bruno/Library/Application Support/Sublime Text 2/Packages/User"
- modification :

        // Pour mettre en majuscule la première lettre du mot sous le curseur
        { "keys": ["super+k", "super+t"], "command": "title_case" }


### C/C++ ###

- but          : Lancer le programme dans l'invite de commande sous Windows
- fichier      : C++.sublime-build
- localisation : "C:\Users\Bruno\AppData\Roaming\Sublime Text 2\Packages\C++\"
- modification :

        "windows": {
                   "cmd": ["cmd.exe", "/c", "${file_path}\\\\${file_base_name}.exe"]
        }


### SmartMarkdown ###

- but          : Ne garder que les raccourcis utiles
- fichier      : Default.sublime-keymap
- localisation : "C:\Users\Bruno\AppData\Roaming\Sublime Text 2\Packages\SmartMarkdown"
- modification : tout commenter sauf "smart\_folding" et "global\_folding"


### Markdown Preview ###

- but          : Créer un raccourci pour l'aperçu dans le navigateur
- fichiers     : Default (Windows).sublime-keymap, Default (OSX).sublime-keymap
- localisation : ...\Packages\User
- modification :

        { "keys": ["alt+m"], "command": "markdown_preview", "args": {"target": "browser", "parser":"markdown"} }


- but          : recharcher la page du navigateur quand on enregistre un fichier markdown .txt
- fichier      : MarkdownPreview.sublime-settings
- localisation : "C:\Users\Bruno\AppData\Roaming\Sublime Text 2\Packages\Markdown Preview"
- modification : (ajout de l'extension ".txt")

        /*
            Sets the supported filetypes for auto-reload on save
        */
        "markdown_filetypes": [".md", ".markdown", ".mdown", ".txt"],


### Markdown Editing ###

- but          : ajouter les dièses à la fin des titres
- fichiers     : "Markdown (Standard).sublime-settings", "Markdown.sublime-settings", "MultiMarkdown.sublime-settings", 
- localisation : "C:\Users\Bruno\AppData\Roaming\Sublime Text 2\Packages\Markdown Editing"
- modification : 

        // Automatically switches list bullet when indenting blank list item with <Tab>.
        "mde.list_indent_auto_switch_bullet": true,


- but          : ajouter les fichiers .txt à Markdown Editing
- fichier      : "Markdown.sublime-settings"
- localisation : "C:\Users\Bruno\AppData\Roaming\Sublime Text 2\Packages\Markdown Editing"
- modification :

        "extensions":
        [
            "md",
            "mdown",
            "txt"
        ],


### VBScript ###

- but          : Lancer le script en mode fenêtre (WScript)
- fichiers     : VBScript.sublime-build 
- localisation : "C:\Users\Bruno\AppData\Roaming\Sublime Text 2\Packages\VBScript"
- modification : (suppression de "with WScript" dans name)

        "variants":
        [
            {
                "name": "Run",
                "windows":
                {
                    "cmd": ["wscript.exe", "$file"]
                }
            }
        ]

- but          : Supprimer le problème d'encodage UTF-8 lors du build
- fichiers     : VBScript.sublime-build 
- localisation : "C:\Users\Bruno\AppData\Roaming\Sublime Text 2\Packages\VBScript"
- modification : (ajout de la ligne)

        "cmd": [ "cscript.exe", "$file" ],
        "encoding": "cp1252"

### Mes préférences ###

Je n'utilise pas la même police ni le même thème sur Windows et mac; donc les fichiers Preferences.sublime-settings sont différents.

- fichier : Preferences.sublime-settings
- OS : OSX
- Modifications :

    {
        "color_scheme": "Packages/Color Scheme - Default/Monokai Bright.tmTheme",
        "font_face": "MonacoB2",
        "font_size": 12.0,
        "highlight_modified_tabs": true,
        "ignored_packages":
        [
            "Markdown",
            "Vintage"
        ],
        "log_commands": true,
        "log_input": true,
        "tab_size": 4
    }

- fichier : Preferences.sublime-settings
- OS : OSX
- Modifications :

    {
      "color_scheme": "Packages/Color Scheme - Default/Monokai Bright.tmTheme",
      "font_face": "Consolas",
      "font_size": 11,
      "highlight_modified_tabs": true,
      "ignored_packages":
      [
        "Vintage"//,
        // "Package Control",
        // "MarkdownEditing",
        // "Markdown Preview",
        // "SmartMarkdown",
        // "VBSript",
        // "orgmode",
        // "mdTodo/MarkdownT",
        // "FindKeyConflicts",
        // "PowerShell"
      ]
    }


### Modification du raccourci clavier pour afficher la console ##

Le but : utiliser "ctrl+ù" au lieu de "ctrl+`" (qui ne fonctionne pas, voir ci-dessous comment tracer les raccourcis clavier).

Il faut modifier le fichier Default (OSX).sublime-keymap pour y ajouter:

    // Console : Modification du raccourci pour afficher la console : Ctrl + ù
    // (au lieu de Ctrl + ` qui ne fonctionne pas sur un clavier Fr)

    { "keys": ["ctrl+ù"], "command": "show_panel", "args": {"panel": "console", "toggle": true} },


__Tracer les commandes (pour connaître la commande d'affichage de la console):__
        
        sublime.log_commands(True)

__Tracer les raccourcis clavier (pour voir ce qui est reçu quand on tape "ctrl+`"):__

        sublime.log_input(True)

- fichier : Default (OSX).sublime-keymap
- but     : remplacer le raccouris pour afficher la console
- modification :



## Liens intéressants

- [Sublime Text Introduction (Tutorial #1)](https://www.youtube.com/watch?v=SVkR1ZkNusI)
- [Sublime Text 2 Documentation](https://www.sublimetext.com/docs/2/index.html)
- [WorkFlows](http://www.smashingmagazine.com/2013/10/powerful-workflow-tips-tools-and-tricks-for-web-designers/)
- [How to Create a Sublime Text 2 Plugin](http://code.tutsplus.com/tutorials/how-to-create-a-sublime-text-2-plugin--net-22685)
- [How to Add a Shortcut for Any Command in Sublime Text](http://brendankemp.com/essays/how-to-add-a-shortcut-for-any-command-in-sublime-text/)
- [Sublime Text 2 – Raccourcis utiles (Windows)](https://gist.github.com/spyl94/3963465)
- [Sublime Text 2 Cheat Sheet](https://www.shortcutfoo.com/app/dojos/sublime-text-2-win/cheatsheet)
- [Exporting Sublime Text configuration and installed packages](http://stackoverflow.com/questions/16412678/exporting-sublime-text-configuration-and-installed-packages)
- [Exporting and sharing Sublime Text configuration](http://opensourcehacker.com/2013/05/09/exporting-and-sharing-sublime-text-configuration/)
- [Configurer Sublime Text en 30 secondes grâce à git](https://blog.smarchal.com/configurer-sublime-text-en-30-secondes-grace-a-git#que-faut-il-sauvegarder-)
