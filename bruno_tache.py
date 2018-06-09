# +---------------------------------------------------------------------------+
# | Crée une tâche ou la termine.                                             |
# | ex : - [ ] Aller à la piscine                                             |
# |      - [X] Faire le ménage                                                |
# +---------------------------------------------------------------------------+

# +---------------------------------------------------------------------------+
# |  Fichier     : bruno_tache.py                                             |
# |  Version     : 1.0.0                                                      |
# |  Auteur      : Bruno Boissonnet                                           |
# |  Date        : 08/06/2018                                                 |
# +---------------------------------------------------------------------------+

import sublime, sublime_plugin

ALLOWED_FILETYPES = ('.md', '.markdown', '.mdown', '.txt')
DEBUG = False


class BrunoBase(sublime_plugin.TextCommand):
    def pdebug(self, message):
        if DEBUG:
            print(message)
    def run(self, edit):
        filename = self.view.file_name()
        # list of allowed filetypes
        if not (filename or filename.endswith(ALLOWED_FILETYPES)):
            return False
        self.run(edit)


class BrunoTerminerTacheCommand(BrunoBase):
    # """Termine une tâche"""

    def run(self, edit):
        for region in self.view.sel():
            if region.empty():
                # sublime.message_dialog("Région vide")
                self.pdebug("Région vide")
                lines = self.view.lines(region)
                self.pdebug("Une seule ligne (%d)" % len(lines))
                for line in lines:
                    # On récupère le contenu de la ligne
                    line_contents = self.view.substr(line).strip()
                    self.pdebug("Contenu de la ligne : %s" % line_contents)
                    if line_contents.startswith("- [ ]"):
                        # La ligne est une tâche non terminée
                        self.pdebug("La ligne est une tâche non terminée")
                        # On récupère la région contenant "[ ]"
                        line_undone = self.view.find("\[ \]", line.begin())
                        # On y insère "[X]"
                        self.view.replace(edit, line_undone, "[X]")
                        self.pdebug("La ligne est désormais une tâche non terminée")
                        line_contents = self.view.substr(line).strip()
                        self.pdebug("Contenu de la ligne : %s" % line_contents)
                    else:
                        self.pdebug("La ligne est une tâche terminée")
                        # On récupère la région contenant "[X]"
                        line_done = self.view.find("\[X\]", line.begin())
                        # On remplace cette région par "[ ]"
                        self.view.replace(edit, line_done, "[ ]")
                        self.pdebug("La ligne est désormais une tâche non terminée")
                        line_contents = self.view.substr(line).strip()
                        self.pdebug("Contenu de la ligne : %s" % line_contents)

            else:
                self.pdebug("Région non vide => Sélection")
                self.pdebug("Nombre de lignes sélectionnées : %d" % len(lines))
                lines = self.view.lines(region)
                # lines.reverse()
                for line in lines:
                    line_head = self.view.find("[-\+]", line.begin())
                    line_done = self.view.find("\[X\]", line.begin())
                    line_undone = self.view.find("\[ \]", line.begin())
                    line_contents = self.view.substr(line).strip()
                    if not line_done:
                        self.view.replace(edit, line_undone, "[X]")
                        break
                    else:
                        self.view.replace(edit, line_done, "[ ]")
                        break


class BrunoNouvelleTacheCommand(BrunoBase):
    def run(self, edit):
        # print("coucou")
        for region in self.view.sel():
            lines = self.view.lines(region)
            lines.reverse()
            self.pdebug("Plusieurs lignes (%d)" % len(lines))
            for line in lines:
                if not line:
                    line_contents = '- [ ] '
                    self.view.insert(edit, line.begin(), line_contents)
                    self.pdebug("Création d'une tâche dans une ligne vide (%s)" % line_contents)
                else:
                    line_head = self.view.find("[-\+]", line.begin())
                    line_contents = self.view.substr(line).strip()
                    self.pdebug("Création d'une tâche dans une ligne non vide (%s)" % line_contents)
                    # prepend @done if item is ongoing
                    if line_contents.startswith('-'):
                        self.pdebug("1- La ligne commence par \"- \" : %s" % line_contents)
                        if line_contents.startswith('- [ ]'):
                            self.pdebug("1b- La ligne commence par \"- [ ]\" : %s" % line_contents)
                        else:
                            self.view.replace(edit, line_head, "- [ ]")
                    else:
                        self.pdebug("2- La ligne ne commence par \"- \" : %s" % line_contents)
                        line_contents = '- [ ] ' + self.view.substr(line)
                        self.view.replace(edit, line, line_contents)
