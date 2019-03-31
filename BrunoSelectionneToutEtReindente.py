
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


import sublime, sublime_plugin, datetime, locale

class BrunoSelectionneToutEtReindenteCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("select_all")
        self.view.run_command("reindent")
        self.view.run_command("invert_selection")

