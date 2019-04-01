
# +---------------------------------------------------------------------------+
# | Sélectionne tout et réindente.                                            |
# | ex : Mardi 15 Octobre 2015                                                |
# | ex : 13:54                                                                |
# +---------------------------------------------------------------------------+

# +---------------------------------------------------------------------------+
# |  Fichier     : bruno_date.py                                              |
# |  Version     : 1.1.0                                                      |
# |  Auteur      : Bruno Boissonnet                                           |
# |  Date        : 08/06/2018                                                 |
# +---------------------------------------------------------------------------+


import sublime, sublime_plugin

DEBUG = False

class BrunoSelectionneToutEtReindenteCommand(sublime_plugin.TextCommand):
    def pdebug(self, message):
        if DEBUG:
            print(message)


    def run(self, edit):
        point = self.view.sel()[0].begin()  # Enregistre la position du curseur
        self.pdebug(point)
        self.view.run_command("select_all")
        self.view.run_command("reindent")
        self.view.run_command("invert_selection")
        self.view.sel().clear()
        self.view.sel().add(point)          # Remets le curseur à sa place AVANT la réindentation (donc pas forcément à la même place )

