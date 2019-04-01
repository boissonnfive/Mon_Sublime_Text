# Sublime Text

## Présentation

C'est un éditeur que j'utilise pour écrire des notes (principalement en Markdown). Je voudrais bien le maîtriser aussi bien que TextMate avec lequel je sais bien coder en HTML/CSS/PHP.


## Les raccourcis que j'utilise

Pour obtenir les raccourcis sur mac, il faut remplacer Ctrl par ⌘, sauf quand il y a un astérisque (*) dans le raccourci. Dans les autres cas, le raccourci mac est écrit.

**Si on ne doit retenir qu'un seul raccourci, c'est celui de la palette de commande : ⌘ ⇧ P**


### Génériques ###

- Passer en majuscule                                       : ⌘ K U
- Passer en minuscule                                       : ⌘ K L
- Mettre la première lettre en majuscule                    : ⌘ K T [1]
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
- Aligner les : ou = dans une sélection de lignes           : ⌘ ⌃ A [2]
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


---
- [1]: si on met :{ "keys": ["ctrl+k", "ctrl+t"], "command": "title_case" } dans ses préférences utilisateur
- [2]: nécessite le module *Alignment*


### C/C++ ###

- Compiler le fichier (créer un fichier .exe)                  : ⌘ B
- Lancer le fichier (la sortie est affichée dans Sublime Text) : ⌘ ⇧ B
- Indenter                                                     : ⌘ )
- Désindenter                                                  : ⌘ ^


## Les astuces

### Créer un projet ###

1. Mettre tous les fichiers de son projet dans un dossier
1. Ajouter ce dossier à votre projet (qui va ainsi être créé): **Project > Add Folder to Project…** (Les fichiers du dossier doivent maintenant apparaître dans la barre latérale)
1. Enregistrer le projet: **Project > Save Project As…**. 2 fichiers sont créés:

        your_project.sublime-project
        your_project.sublime-workspace


### Ouvrir un fichier en hexadécimal ###

1. Menu File > Reopen with Encoding
2. Hexadecimal


### Les dossiers de configuration ###

- Windows : %APPDATA%\Sublime Text 3
- OS X    : ~/Library/Application Support/Sublime Text 3
- Linux   : ~/.config/sublime-text-3


### Taper des commandes python ###

Aller dans la console (Ctrl+ù) ou View -> Show Console et taper :

    sublime.version()


### Modifier le raccourci d'une commande (ex: afficher la console)

Sur un clavier AZERTY, il est impossible de tape le raccourci "ctrl+`". Pour afficher la console, on peut modifier ce raccourci pour qu'il devienne : "ctrl+ù".

#### 1. Récupérer le nom de la commande qui affiche la console :

1. Ouvrir la console par le menu
2. Dans la console, taper :
    
        sublime.log_commands(True)
        sublime.log_input(True) # trace les raccourcis clavier

3. Aller dans le menu et ouvrir la console
4. Récupérer le nom de la commande dans la console

#### 2. Créer un raccourci pour cette commande

1. Ouvrir le fichier Default (OSX).sublime-keymap (pour OSX, sinon prendre celui de Windows)
2. Taper la ligne suivante :

        { "keys": ["ctrl+ù"], "command": "show_panel", "args": {"panel": "console", "toggle": true} },


## Créer une commande dans Sublime Text

### Le squelette de la commande

*NOTE: ATTENTION aux tabulations en Python => Il faut des espaces.*

    import sublime, sublime_plugin
         
    class UnNomDeCommandeCommand(sublime_plugin.TextCommand):
        def run(self, edit):

À enregistrer dans un fichier .py dans le dossier Packages/User.


### Quelques variables utiles

    ${packages} # => renvoi le chemin complet du dossier "packages"

### Quelques fonctions utiles

    # Affiche une boîte de dialogue
    sublime.message_dialog("Région vide")
    # Affiche dans la console
    print("Plusieurs lignes (%d)" % len(lines))
    
    # Ouvre un fichier du dossier $packages/User
    sublime.active_window().run_command("open_file", { "file": "${packages}/User/Sublime Text.md"})
    
    # Récupère la sélection
    for region in self.view.sel():
    
    # Récupère les lignes ( ie des Régions)
    lines = self.view.lines(region)
    
    # Récupère le contenu de la ligne
    if region.empty():
        line = self.view.line(region)
        line_contents = self.view.substr(line)
    
    # Insère dans la ligne en cours
    self.view.insert(edit, line.begin(), line_contents)
    
    # Remplace la ligne en cours (line) par une chaine (line_contents)
    self.view.replace(edit, line, line_contents)
    
    # Efface la chaîne en paramètre
    self.view.erase(edit, chaine)



## Ma config

### Paquets installés (28)

[*Remarque : ⌘ + ⇧ + P (command palette) + list package*]

- **A File Icon**           : Ensemble d'icônes pour Sublime Text
- **Alignment**             : Aligne le texte selon : ou =
- **AutoFileName**          : Insére un nom de fichier automatiquement
- **Color Highlight**       : Affiche la couleur d'une valeur dans le CSS
- **ColorPicker**           : Affiche une dialogue de sélection de couleur
- **Colorsublime**          : 
- **Colorsublime - Themes** : 
- **DocBlockr**             : Insére un bloc de commentaire de type JavaDoc
- **Emmet**                 : offre des raccourcis pour le HTML et le CSS
- **FindKeyConflicts**      : Recherche les raccourcis associés à plusieurs paquets
- **Git**                   : Affiche le statut git dans la barre d'état
- **MarkdownEditing**       : Affiche la coloration syntaxique du Markdown
- **MarkdownPreview**       : Affiche le document Markdown dans un navigateur
    + Markdown Preview: Preview in Browser (⌥ M)
    + Markdown Preview: Export HTML in Sublime Text
    + Markdown Preview: Copy to Clipboard
    + Markdown Preview: Open Markdown Cheat sheet
    + Permet d'utiliser son propre modèle HTML
- **MarkdownTodo**   : ajoute des commandes sur les tâches (*Seulement sur ST2*)
- **Material Theme** : installe un thème sombre et bleu turquoise
- **orgmode**        : pour faire du orgmode dans Sublime Text
    + "-c"+tab         : crée une liste non cochée
    + Entrer           : coche la case à cocher
- **Package Control** : installateur de paquets pour Sublime Text
- **PowerShell**      : 
- **PyV8**            :
- **Settings**        :
- **SideBarEnhancements**  : Ajoute X actions au menu contextuel de la side bar
- **SmartMarkdown**   : copie le fonctionnement de orgmode pour Markdown
    + Pliage/Dépliage des titres (⇥)
    + Pliage/Dépliage global (Maj + ⇥)
    + Augmente/Diminue le niveau des titres (⌘ ⇧ ; / ⌘ ⇧ ,)
    + Continuation des listes après appuis sur ↩
    + Tableaux intelligents (⇥)
- **SublimeLinter**   : Signale les erreurs dans le code
- **SublimeServer**   : Lance un serveur HTTP
- **Terminus**        : Affiche le Terminal dans Sublime Text (un panneau en bas)
- **UnicodeNormalizer**   : Transforme un fichier UTF-8 en Unicode Normalization Form C (pour la validation W3C)
- **VBScript**            : affiche la coloration syntaxique du VBScript + snippets
- **View In Browser**     : Affiche le contenu du fichier dans un navigateur
- **zzz A File Icon zzz** : Ensemble d'icônes pour Sublime Text (modifié pour le Material Theme)

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
- OS : Windows
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
