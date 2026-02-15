from guerrier import Guerrier
import random

class Berserker(Guerrier):
    """constructeur

    Args:
        Guerrier (_type_): _description_
    """

    #constructeur
    def __init__(self, nom: str, vie: int, attaque: int, force: int):
        super().__init__(nom, vie, attaque, force)

    def attaquer(self) -> float:
        """formule de l'attaque

        Returns:
            float: retourne l'attaque
        """
        degat = self.attaque + (self.force / 2) + random.randint(-2,2)

        #calcul bonus
        attaque_bonus = ((self.vie_max - self.vie) // 10) * 5

        degat_attaque = degat + attaque_bonus

        return degat_attaque
    
    
    def subir_degat(self, degat : int) -> None:
        """calculer les dégatas

        Args:
            degat (int): dégats que subit le personnage
        """
        degat_final = degat - self.armure.points_armure
        if degat_final > 0:
            self.vie -= degat_final

        #si 50% de vie et moins
        if self.vie <= self.vie // 2 :
            print(f"Le Berserker {self.nom} entre en FUREUR !")