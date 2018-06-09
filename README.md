# Mon_Sublime_Text

Mes paramètres, mes notes et mes codes pour Sublime Text.

## Les fichiers

- __Sublime Text.md__ : mes notes sur Sublime Text.
- __raccourcis.md__ : liste non exhaustive des raccourcis clavier de Sublime Text.
- __Default (XX).sublime.keymap__ : mes propres raccourcis clavier.
- __Package Control.sublime-settings__ : la liste des paquets installés.
- __Package Control Messages.md__ : les README des paquets installés.
- __XXX.sublime-settings__ : mes paramètres de configuration.
- __bruno_date.py__ : commandes perso pour ajouter la date ou l'heure.
- __bruno_tache.py__ : commandes perso pour créer une tâche ou la terminer.
- __.gitignore__ : ne rien récupérer sauf le dossier User.
- __Bruno.sublime-commands__ : Pour afficher mes commandes personnelles dans la palette de commande.
- __HTML-Template.sublime-snippet__ : Snippet pour créer un squelette de fichier HTML.
- __context.sublime-menu__ : Pour afficher mes commandes personnelles dans le menu contextuel.

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

