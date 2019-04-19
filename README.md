# Mon Sublime Text

![Sublime Text 3 Logo](ST3_Logo.png)

Mes paramètres, mes notes et mes codes pour Sublime Text.

## Table des matières

<!-- MarkdownTOC -->

- [Les fichiers du projet](#user-content-les-fichiers-du-projet)
- [Mettre ses paramètres ST sur GitHub](#user-content-mettre-ses-paramètres-st-sur-github)
- [Installer ses paramètres après une nouvelle installation de ST](#user-content-installer-ses-paramètres-après-une-nouvelle-installation-de-st)

<!-- /MarkdownTOC -->


## Les fichiers du projet

- __.gitignore__ : ne récupére que les fichiers suivants et .gitignore.
- __Base File.sublime-settings__ : config du paquet alignment
- __Batch File.tmLanguage__ : ma modif du langage Batch.
- __Bruno.sublime-commands__ : Pour afficher mes commandes personnelles dans la palette de commande.
- __Bruno.sublime-completions__ : Liste de mots à ajouter à la completion de ST.
- __Color Highlight.sublime-settings__ : config « Color Highlight »
- __Dark-Dracula_BB.tmTheme__ : Mes modifs du theme Dark-Dracula
- __Default (XX).sublime.keymap__ : mes propres raccourcis clavier.
- __Gist.sublime-settings__ : config Gist
- __HTML-Template.sublime-snippet__ : Snippet pour créer un squelette de fichier HTML.
- __Markdown (Standard).sublime-settings__ : config MarkdownEditing.
- __MarkdownPreview.sublime-settings__ : config MarkdownPreview.
- __MarkdownTOC.sublime-settings__ : config MarkdownTOC
- __Material-Theme-Darker.sublime-theme__ : modifs du thème Material Darker.
- __Material-Theme-Darker.tmTheme__ : modifs du thème Material Darker.
- __Mon_Sublime_Text.sublime-project__ : fichier projet Sublime Text
- __Mon_Sublime_Text.sublime-workspace__ : fichier workspace du projet
- __Package Control Messages.md__ : les README des paquets installés.
- __Package Control.sublime-settings__ : la liste des paquets installés.
- __PlainTasks.sublime-settings__ : config PlainTasks
- __Preferences.sublime-settings__ : mes paramètres de configuration.
- __README.md__ : ce fichier.
- __Sublime Text.md__ : mes notes sur Sublime Text.
- __SublimeServer.sublime-settings__ : config SublimeServer.
- __VBScript.sublime-build__ : mes modifs dans le build des fichiers VBscript.
- __bruno_date.py__ : commandes perso pour ajouter la date ou l'heure.
- __bruno_reindente.py__ : commandes perso pour réindenter.
- __bruno_tache.py__ : commandes perso pour créer une tâche ou la terminer.
- __context.sublime-menu__ : Pour afficher mes commandes personnelles dans le menu contextuel.
- __raccourcis.md__ : les raccourcis clavier que j'utilise.

## Mettre ses paramètres ST sur GitHub

[source](https://blog.smarchal.com/configurer-sublime-text-en-30-secondes-grace-a-git#que-faut-il-sauvegarder-)

    cd %APPDATA%/Sublime Text 3
    # ou cd "~/Library/Application Support/Sublime Text 3"
    git init
    # Créer un fichier .gitignore (voir le dépôt)
    git remote add origin https://github.com/<user>/st3-settings.git
    git add --all
    git commit -m "Ma sauvegarde Sublime Text 3"
    git push origin master


## Installer ses paramètres après une nouvelle installation de ST

    cd %APPDATA%/Sublime Text 3
    # ou cd "~/Library/Application Support/Sublime Text 3"
    git init
    git remote add origin https://github.com/<user>/st3-settings.git
    git fetch
    git checkout -t origin/master

