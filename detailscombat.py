from personnage import Personnage

class Detailscombat:
    """classe qui détails les combats
    """
    #constructeur
    def __init__(self, nom_perso_1 : str, nom_perso_2 : str):
        self.nom_perso_1 = nom_perso_1
        self.nom_perso_2 = nom_perso_2
        self.vainqueur = ""
        self.nb_tours = 0

    def incrementer_tour(self) -> None:
        """sert à calculer le nombre de tours que dur le combat
        """
        self.nb_tours += 1

    def nom_vainqueur(self, vainqueur : Personnage) -> None:
        """sert à déterminer le vainqueur

        Args:
            vainqueur (Personnage): vainqueur du combat
        """
        self.vainqueur = vainqueur.nom

    def __str__(self) -> str:
        """sert à imprimer le combat

        Returns:
            str: imprimer les détails du combat
        """
        return f"Premier combatant: {self.nom_perso_1}, deuxième combatant: {self.nom_perso_2}. Le combat à duré {self.nb_tours} tours et c'est {self.vainqueur} qui à remporter le combat"