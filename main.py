
taches = []

def ajouter_tache():
    titre = input("Donner le titre de la tâche : ")

    if titre.strip() == "":
        print("Erreur : titre vide !")
    else:
        numero = len(taches) + 1
        tache = {"numero": numero, "titre": titre}
        taches.append(tache)
        print("Tâche ajoutée avec succès !")


def afficher_taches():
    if len(taches) == 0:
        print("Aucune tâche disponible.")
    else:
        print("\n===== LISTE DES TACHES =====")
        for tache in taches:
            print(tache["numero"], "-", tache["titre"])


def rechercher_tache():
    mot_cle = input("Donner un mot-clé : ")
    trouve = False

    for tache in taches:
        if mot_cle.lower() in tache["titre"].lower():
            print(tache["numero"], "-", tache["titre"])
            trouve = True

    if trouve == False:
        print("Aucune tâche trouvée.")


while True:
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Ajouter une tâche")
    print("2 - Afficher les tâches")
    print("3 - Rechercher une tâche")
    print("0 - Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
        ajouter_tache()
    elif choix == "2":
        afficher_taches()
    elif choix == "3":
        rechercher_tache()
    elif choix == "0":
        print("Merci d'avoir utilisé notre application.")
        break
    else:
        print("Erreur : choix invalide.")
