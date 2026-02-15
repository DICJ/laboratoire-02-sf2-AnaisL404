from archer import Archer
from guerrier import Guerrier
from mage import Mage
from arene import Arene
from soldat import Soldat
from berserker import Berserker



def menu() -> None:
    print("1. Ajouter un personnage")
    print("2. Voir les personnages dans l'arène")
    print("3. Faire combattre deux personnages")
    print("4. Afficher l'historique de combats")
    print("5. Nettoyer l'arène")
    print("6. Voir le nombre de combatants dans l'arène")
    print("7. Lancer le battle royal")
    print("0. quitter")

choix = 100000000
arene1 = Arene()


while choix != 0:
    print()
    menu()
    choix = int(input("Entrez un nombre (0 pour quitter): ")) 

    match choix:
        #créé un personnage
        case 1:
            print()
            nom = input("Entrez le nom du personnage: ")
            vie = int(input("Entrez les points de vie du personnage: "))
            attaque = int(input("Entrez la puissance de l'attaque: "))

            sorte = input("Que voulez-vous créer?(archer, guerrier, mage, soldat, berserker): ")

            #définir le l'argument spécial
            if sorte == "archer":
                dexterite = int(input("Entrez la dexteriter du personnage: "))
                nouveau_perso = Archer(nom, vie, attaque, dexterite)
            elif sorte == "guerrier":
                force = int(input("Entrez la force du personnage: "))
                nouveau_perso = Guerrier(nom, vie, attaque, force)
            elif sorte == "mage":
                mana = int(input("Entrez le nombre de mana du personnage: "))
                nouveau_perso = Mage(nom, vie, attaque, mana)
            elif sorte == "soldat":
                nouveau_perso = Soldat(nom, vie, attaque)
            elif sorte == "berserker":
                force = int(input("Entrez la force du personnage: "))
                nouveau_perso = Berserker(nom, vie, attaque, force)
            else:
                print("choix invalide, réessayez")

            arene1.ajouter_personnage(nouveau_perso)
        #afficher perso
        case 2:
            print()
            arene1.afficher_personnage()
        #faire un combat
        case 3:
            print()
            if len(arene1.lst_perso) < 2:
                print("Il doit avoir minimun 2 personnages de créé pour fairre un combat")
                print("Créé un nouveau personnage")
            else:
                arene1.afficher_personnage()
                print()
                index1 = int(input("Entrez le numéro du combatant 1: "))
                index2 = int(input("Entrez le numéro du combatant 2: "))
                print()

                combatant1 = arene1.lst_perso[index1]
                combatant2 = arene1.lst_perso[index2]
                
                arene1.combat(combatant1, combatant2)
        #voir l'histirique des combats
        case 4:
            print()
            for combat in arene1.lst_historique_combats:
                print(combat)
        #nattoyer l'arène
        case 5:
            print()
            arene1.nettoyer_arene()
            print("L'arène à été nettoyer !")
        #voir le nombre de combatants
        case 6:
            print()
            print(f"Il y a {arene1.__len__()} combatants dans l'arène")
        #faire un battle royal
        case 7:
            print()
            if len(arene1.lst_perso) < 2:
                print("Il doit avoir minimun 2 personnages de créé pour fairre un combat")
                print("Créé un nouveau personnage")
            else:
                arene1.lancer_battle_royal()