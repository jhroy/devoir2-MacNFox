# coding: utf-8
# Importation des fichiers CSV, JSON et REQUESTS

import csv
import json
import requests

fichier = "lobby.csv"
fichier = "lobby-JHR.csv"
url = "http://jhroy.ca/uqam/lobby.json"

# Qui suis-je ?
entetes = {
    "User-Agent":"David Masse - 438/ 837-9870: requête envoyéee dans le cadre d'un cours de journalisme à l'UQAM",
    "From":"davidmasseyt@hotmail.com"
}

req = requests.get(url,headers=entetes)
# print(req)

# Est-ce que ça marche?
# req = requests.get(fichier, headers=entetes)
# print (req)
# Tout est correct, j'obtiens la combinaison gangnante [200]

if req.status_code == 200:
     print("bonheur d'occasion") ### HAHA!

# Mes raccourcis

n = 0
board = []

# Mes informations de boucle |>o<|
# Création d'une boucle, afin de tout extraire 

# for number in range[0,72001]: ### CETTE BOUCLE NE MARCHE PAS -> POUR GÉNÉRER UN "RANGE", ON MET LES NOMBRES ENTRE PARENTHÈSES PCQ RANGE EST UNE FONCTION, NON PAS ENTRE CROCHETS
for number in range(0,72001):
    n+=1
    comm=req.json()
    req = requests.get(url, headers=entetes) ### TU VAS TE CONNECTER À MON SITE 72000 FOIS, ICI...
    info = []
    info.append(n) ### "INFO" N'EST PAS DÉFINIE, ALORS JE L'AI FAIT À LA LIGNE JUSTE AVANT
    # info.append(nb) ### CETTE VARIABLE N'EXISTE PAS DANS CE SCRIPT, ALORS ON MET CETTE LIGNE EN COMMENTAIRE
    print(info)
#     # Mes conditions et mes valeurs qui sont à afficher
#     if "limat" in comm["registre"][0][1][0]["objet"]:
#         # Création de ma liste 1
#        liste1 = {
#            'num' : comm["registre"][0][0]["client_org_corp_num"],
#            'nom' : comm["registre"][0][0]["fr_client_org_corp_nm"],
#            'name' : comm["registre"][0][0]["en_client_org_corp_nm"],
#            'date' : comm["registre"][0][0]["date_comm"],
#            'sujet principal' : comm["registre"][0][1][0]["objet"],
#            'sujet autre' : comm["registre"][0][1][0]["objet_autre"],
#            'institution' : comm["registre"][0][2][0]["institution"],
#            }
#     elif "limat" in comm["registre"][0][1][1]["objet"]
#     # Création de ma liste 2 
#           liste2 = {
#            'num' : comm["registre"][0][0]["client_org_corp_num"],
#            'nom' : comm["registre"][0][0]["fr_client_org_corp_nm"],
#            'name' : comm["registre"][0][0]["en_client_org_corp_nm"],
#            'date' : comm["registre"][0][0]["date_comm"],
#            'sujet principal' : comm["registre"][0][1][1]["objet"],
#            'sujet autre' : comm["registre"][0][1][1]["objet_autre"],
#            'institution' : comm["registre"][0][2][0]["institution"],
#            }
#     elif "limat" in comm ["registre"][0][1][2]["objet"]
#     # Création de ma liste 3
#         liste3 = {
#            'num' : comm["registre"][0][0]["client_org_corp_num"],
#            'nom' : comm["registre"][0][0]["fr_client_org_corp_nm"],
#            'name' : comm["registre"][0][0]["en_client_org_corp_nm"],
#            'date' : comm["registre"][0][0]["date_comm"],
#            'sujet principal' : comm["registre"][0][1][2]["objet"],
#            'sujet autre' : comm["registre"][0][1][2]["objet_autre"],
#            'institution' : comm["registre"][0][2][0]["institution"],
#            }
# # Je viens clore ma boucle en demandant à Python d'exporter mes informations 
#         board.append(liste1)
#         board.append(liste2)
#         board.append(liste3)
#         dead = open(fichier,"a")
#         obies = csv.writer(dead)
#         obies.writerow(board)

# # J'ai une erreur de syntaxe à la ligne 54, mais je ne trouve pas l'erreur,
# # j'en suis désolé. 

# # Notes pour ne pas tout réécrire si je modifie de quoi entre-temps
# # print (obj["registre"][0][0]["fr_client_org_corp_nm"])
# # print (obj["registre"][0][0]["en_client_org_corp_nm"])
# # print (obj["registre"][0][0]["client_org_corp_num"])
# # num = obj["registre"][0][0]["client_org_corp_num"])