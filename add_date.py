#coding=utf-8
# Module pour insérer la date du jour au format :
# Nom_du_jour Numéro_de_jour Nom_du_mois Année
# ex : Mardi 15 Octobre 2015
# Remarques :
#   - On est obligé de remplacer les mois, car les mois ont des accents et ceux-ci
#     ne sont pas gérés par python (version 2.6)
#   - Pour utiliser les accents, ont déclare l'encodage en UTF-8
#   - On peut aussi définir la localisation avec locale
#

import datetime, getpass
import sublime, sublime_plugin 

#print time.localtime()
jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
mois = ["Janvier", u"Février", "Mars", "Avril", "Mai", "Juin", "Juillet", u"Août", "Septembtre", "Octobre", "Novembre", u"Décembre"]


class AddDateCommand(sublime_plugin.TextCommand):
    def run(self, edit):

    	mois_en_cours = mois[datetime.date.today().month-1]
    	date_en_cours = jours[datetime.date.today().weekday()] + datetime.date.today().strftime(" %d ") + mois_en_cours + datetime.date.today().strftime(" %Y")
        self.view.run_command("insert_snippet", { "contents": "%s" %  date_en_cours } )

class AddTimeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet", { "contents": "%s" %  datetime.datetime.now().strftime("%H:%M") } )