from personnage import Personnage
import time
from detailscombat import Detailscombat

class Arene:
    """cette classe représente l'arène
    """

    #constructeur
    def __init__(self):
        self.lst_perso : list[Personnage]= []
        self.lst_historique_combats = []

    def ajouter_personnage(self, personnage : Personnage) -> None:
        """sert à ajouter un personnage dans la liste

        Args:
            personnage (Personnage): personnage à mettre dans la liste
        """
        self.lst_perso.append(personnage)

    def afficher_personnage(self) -> None:
        """afficher les personnage
        """
        cpt = 0
        for perso in self.lst_perso:
            print(f"{cpt} - {perso}")
            cpt += 1

    def combat(self, combatant1 : Personnage, combatant2 : Personnage) -> None:
        """fait un combat entre 2 personnages

        Args:
            combatant1 (Personnage): combatant 1
            combatant2 (Personnage): combatant 2
        """
        details_combat = Detailscombat(combatant1.nom, combatant2.nom)

        while combatant1.vie > 0 and combatant2.vie > 0:
            degat = combatant1.attaquer()
            combatant2.subir_degat(degat)
            print(f"{combatant1.nom} inflige {degat} dégâts à {combatant2.nom}")

            #vérifier si le combatant à encore de la vie
            if combatant2.vie > 0:
                degat2 = combatant2.attaquer()
                combatant1.subir_degat(degat2)
                print(f"{combatant2.nom} inflige {degat} dégâts à {combatant1.nom}")
            details_combat.incrementer_tour()

        #établir le gagnant
        if combatant1.vie > 0:
            vainqueur = combatant1
        else:
            vainqueur = combatant2
        
        details_combat.nom_vainqueur(vainqueur)
        self.lst_historique_combats.append(details_combat)
        time.sleep(1)
        print(f"Le vainqueur du combat est {vainqueur.nom}")
        print()

    def nettoyer_arene(self) -> None:
        """enlève les personnages mort
        """
        for perso in self.lst_perso:
            if perso.vie <= 0:
                #enlever les personnages mort
                self.lst_perso.remove(perso)

    def __len__(self) -> int:
        """calcul combien il y a de personnage dans la liste

        Returns:
            int: retourne la grandeur de la liste
        """
        self.nettoyer_arene()
        return len(self.lst_perso)
        
    def soigner_perso(self, perso: Personnage) -> None:
        """soigne un personnage

        Args:
            perso (Personnage): personnage à soigner
        """
        perso.reset()

    def lancer_battle_royal(self) -> None:
        """faire un battle royal
        """
        #lancer le battle royal
        while len(self.lst_perso) > 1:
            self.lst_perso[0].reset()
            self.combat(self.lst_perso[0], self.lst_perso[1])
            self.nettoyer_arene()
        
        #remettre la vie du gagnant au max
        vainqueur = self.lst_perso[0]
        time.sleep(1)
        print(f"Le vainqueur du battle royal est {vainqueur}")