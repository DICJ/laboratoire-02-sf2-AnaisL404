from personnage import Personnage
from armure import Armure

class Soldat(Personnage):
    """classe soldat

    Args:
        Personnage (_type_): héritage du parent
    """
    #constructeur
    def __init__(self, nom: str, vie: int, attaque: int):
        armure = Armure("cotte de mailles", 15)
        super().__init__(nom, vie, attaque, armure)

    def subir_degat(self, degat) -> None:
        """calcule des dégats à subir

        Args:
            degat (_type_): valeur des dégats
        """
        degat_final = degat - self.armure.points_armure
        #si toute l'armure prend les dégats
        if degat_final < 0:
            degat = 0
        else:
            degat = degat_final * 0,9
