from personnage import Personnage
import random
from armure import Armure
 
class Mage(Personnage):
    """classe du mage

    Args:
        Personnage (_type_): _description_
    """
    #constructeur
    def __init__(self, nom : str, vie :int, attaque :int, mana : int):
        armure = Armure("armure magique", 7)
        super().__init__(nom, vie, attaque, armure)

        self._mana = 0
        self._mana_max = 0

        self.mana = mana
        self.mana_max = mana
        


    #vérification
    @property
    def mana(self) -> int:
        """get le mana

        Returns:
            int: sert à utiliser le mana
        """
        return self._mana
    
    @mana.setter
    def mana(self, mana : int) -> None:
        """vérification du mana

        Args:
            mana (int): mana à valider
        """
       # entre 0 et 100
        if mana >= 0 and mana <= 100:
            self._mana = mana
        # plus petit que 0
        elif mana < 0:
            self._mana = 0
        # plus grand que 100
        elif mana > 100:
            self._mana = 100

    @property
    def mana_max(self) -> int:
        """sert à utiliser le mana max
        Returns:
            int: retourne la mana max
        """
        return self._mana_max
    
    @mana_max.setter
    def mana_max(self, mana_max: int) -> None:
        """vérification du mana max

        Args:
            mana_max (int): mana max à valider
        """
        # entre 0 et 100
        if mana_max >= 0 and mana_max <= 100:
            self._mana_max = mana_max
        # negatif
        elif mana_max < 0:
            self._mana_max = 0
        # plus grand que 500
        elif mana_max > 100:
            self._mana_max = 100

    def diminuer_mana(self) -> None:
        """dimunu le mana après chaque attaque
        """
        self.mana -= random.randint(15,25)


    def attaquer(self) -> int:
        """calculer l'attaque

        Returns:
            int: retourne les dégats que cause l'attaque
        """
        #vérification du niveau de mana
        if self.mana == 0:
           degat_attaque = self.attaque
        else:
            degat_attaque = self.attaque + 60
            self.diminuer_mana()
        return degat_attaque 
    
    def __str__(self) -> str:
        """sert à imprimer le mage

        Returns:
            str: imrpime la derciption du mage
        """
        return f"Le mage {self.nom} à {self.vie} de vie, {self.attaque} d'attaque et {self.mana} de mana"

    def reset(self) -> None:
        """remettre la vie et le mana à son max
        """
        self.vie = self.vie_max
        self.mana = self.mana_max