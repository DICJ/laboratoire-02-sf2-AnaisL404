from personnage import Personnage
import random
from armure import Armure

class Guerrier(Personnage):
    """classe du guerrier

    Args:
        Personnage (_type_): _description_
    """
    #constructeur
    def __init__(self, nom : str, vie :int, attaque :int, force : int):
        armure = Armure("armure de plaques", 12)
        super().__init__(nom, vie, attaque, armure)

        self._force = 0

        self.force = force
        

    #vérification
    @property
    def force(self) -> int:
        """get le force

        Returns:
            int: sert à utiliser la force
        """
        return self._force
    
    @force.setter
    def force(self, force : int) -> None:
        """vérification de la force

        Args:
            force (int): force à valider
        """
        # entre 1 et 50
        if force >= 1 and force <= 50:
            self._force = force
        # negatif
        elif force < 1:
            self._force = 1
        # plus grand que 50
        elif force > 50:
            self._force = 50

    def attaquer(self) -> float:
        """calcule l'attaque

        Returns:
            float: retourne les dégats produit par l'attaque
        """
        degat_attaque = self.attaque + (self.force / 2) + random.randint(-2,2)
        return degat_attaque
    
    def __str__(self) -> str:
        """sert à imprimer le guerrier

        Returns:
            str: retourne la description du guerrier
        """
        return f"Le guérier {self.nom} à {self.vie} de vie, {self.attaque} d'attaque et {self.force} de force"