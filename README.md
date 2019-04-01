# Mon Sublime Text

Mes paramètres, mes notes et mes codes pour Sublime Text.

## Les fichiers

- __Batch File.tmLanguage__ : ma modif du langage Batch.
- __bruno_date.py__ : commandes perso pour ajouter la date ou l'heure.
- __bruno_reindente.py__ : commandes perso pour réindenter.
- __bruno_tache.py__ : commandes perso pour créer une tâche ou la terminer.
- __Bruno.sublime-commands__ : Pour afficher mes commandes personnelles dans la palette de commande.
- __Bruno.sublime-completions__ : Liste de mots à ajouter à la completion de ST.
- __context.sublime-menu__ : Pour afficher mes commandes personnelles dans le menu contextuel.
- __Default (XX).sublime.keymap__ : mes propres raccourcis clavier.
- __HTML-Template.sublime-snippet__ : Snippet pour créer un squelette de fichier HTML.
- __Markdown (Standard).sublime-settings__ : config MarkdownEditing.
- __MarkdownPreview.sublime-settings__ : config MarkdownPreview.
- __Material-Theme-Darker.sublime-theme__ : modifs du thème Material Darker.
- __Material-Theme-Darker.tmTheme__ : modifs du thème Material Darker.
- __Package Control Messages.md__ : les README des paquets installés.
- __Package Control.sublime-settings__ : la liste des paquets installés.
- __Preferences.sublime-settings__ : mes paramètres de configuration.
- __raccourcis.md__ : les raccourcis clavier que j'utilise.
- __README.md__ : ce fichier.
- __Sublime Text.md__ : mes notes sur Sublime Text.
- __SublimeServer.sublime-settings__ : config SublimeServer.
- __VBScript.sublime-build__ : mes modifs dans le build des fichiers VBscript.
- __.gitignore__ : ne récupérer que les fichiers précédents et .gitignore.

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

