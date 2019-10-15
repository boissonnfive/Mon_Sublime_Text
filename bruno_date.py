
# +---------------------------------------------------------------------------+
# | Insére la date ou l'heure du jour.                                        |
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

class BrunoInsereDateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        loc = locale.getlocale(locale.LC_ALL) # get current locale
        # locale.setlocale(locale.LC_ALL,'fr_FR') # Fonctionne sur mac OS
        locale.setlocale(locale.LC_ALL,'french') # Fonctionne sur Windows 10
        self.view.run_command("insert_snippet", { "contents": "%s" %datetime.date.today().strftime("%A %d %B %Y") })
        locale.setlocale(locale.LC_ALL, loc) # restore saved locale

class BrunoInsereHeureCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet", { "contents": "%s" %  datetime.datetime.now().strftime("%Hh%M") })


# +---------------------------------------------------------------------------+
# |                              PYTHON 2.6                                   |
# +---------------------------------------------------------------------------+


# coding=utf-8
# Module pour insérer la date du jour au format :
# Nom_du_jour Numéro_de_jour Nom_du_mois Année
# ex : Mardi 15 Octobre 2015
# Remarques :
#   - On est obligé de remplacer les mois, car les mois ont des accents et ceux-ci
#     ne sont pas gérés par python (version 2.6)
#   - Pour utiliser les accents, on déclare l'encodage en UTF-8
#   - On peut aussi définir la localisation avec locale
#

# import sublime, sublime_plugin, datetime

# jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
# mois = ["Janvier", u"Février", "Mars", "Avril", "Mai", "Juin", "Juillet", u"Août", "Septembtre", "Octobre", "Novembre", u"Décembre"]

# class BrunoInsereDateCommand(sublime_plugin.TextCommand):
#     def run(self, edit):
#         mois_en_cours = mois[datetime.date.today().month-1]
#         date_en_cours = jours[datetime.date.today().weekday()] + datetime.date.today().strftime(" %d ") + mois_en_cours + datetime.date.today().strftime(" %Y")
#         self.view.run_command("insert_snippet", { "contents": "%s" % date_en_cours })

# class BrunoInsereHeureCommand(sublime_plugin.TextCommand):
#     def run(self, edit):
#         self.view.run_command("insert_snippet", { "contents": "%s" %  datetime.datetime.now().strftime("%H:%M") })