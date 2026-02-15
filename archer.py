from personnage import Personnage
import random
from armure import Armure

class Archer(Personnage):
    """classe de l'archer

    Args:
        Personnage (Archer): c'est un archer
    """

    #constructeur
    def __init__(self, nom: str, vie: int, attaque: int, dexterite: int):
        armure = Armure("tunique de cuir", 5)
        super().__init__(nom, vie, attaque, armure)

        self._dexterite = 0

        self.dexterite = dexterite

    #validation
    @property
    def dexterite(self) -> int:
        """get le dexteriter

        Returns:
            int: retourne la dexterité
        """
        return self._dexterite
    
    @dexterite.setter
    def dexterite(self, dexterite : int) -> None:
        """sert à valider la dexterité

        Args:
            dexterite (int): nouvelle dexterité
        """
        # entre 40 et 70
        if dexterite >= 40 and dexterite <= 70:
            self._dexterite = dexterite
        # plus petit 40
        elif dexterite < 40:
            self._dexterite = 40
        # plus grand que 70
        elif dexterite > 70:
            self._dexterite = 70

    def attaquer(self) -> int:
        """équation de l'attaque

        Returns:
            int: retourne l'attaque du personnage
        """
        nb = random.randint(0,100)
        #vérification du niveau de dexteriter
        if nb < self.dexterite:
            degat_attaque = 2 * (self.attaque + 15)
        else:
            degat_attaque = self.attaque + 15
        return degat_attaque
    
    def __str__(self) -> str:
        """sert à imprimer le personnage

        Returns:
            str: retourne le personnage
        """
        return f"L'archer {self.nom} à {self.vie} de vie, {self.attaque} d'attaque et {self.dexterite} de dexteriter"
