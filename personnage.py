from armure import Armure

class Personnage:
    """classe du personnage
    """
    #constructeur
    def __init__(self, nom :str, vie :int, attaque : int, armure: Armure):
        #initialisation
        self.nom = nom
        self._vie = 0
        self._attaque = 0
        self.armure = armure
        self._vie_max = 0

        #vérification
        self.vie = vie
        self.attaque = attaque
        self.vie_max = vie
        

    #vériification
    @property
    def vie(self) -> int:
        """sert à utiliser la vie

        Returns:
            int: vie à utiliser
        """
        return self._vie
    
    @vie.setter
    def vie(self, vie: int) -> None:
        """vérification de la vie

        Args:
            vie (int): vie à valider
        """
        # entre 0 et 500
        if vie >= 0 and vie <= 500:
            self._vie = vie
        # negatif
        elif vie < 0:
            self._vie = 0
        # plus grand que 500
        elif vie > 500:
            self._vie = 500


    @property
    def attaque(self) -> int:
        """sert à utiliser l'attaque

        Returns:
            int: attaque à utiliser
        """
        return self._attaque
    
    @attaque.setter
    def attaque(self, attaque :int) -> None:
        """vérification de l'attaque

        Args:
            attaque (int): attaque à valider
        """
        # entre 0 et 50
        if attaque >= 0 and attaque <= 50:
            self._attaque = attaque
        # negatif
        elif attaque < 0:
            self._attaque = 0
        # plus grand que 50
        elif attaque > 50:
            self._attaque = 50

    @property
    def vie_max(self) -> int:
        """utiliser la vie max

        Returns:
            int: retourne la vie max
        """
        return self._vie_max
    
    @vie_max.setter
    def vie_max(self, vie_max: int) -> None:
        """vérification de la vie max

        Args:
            vie_max (int): vie max à valider
        """
        # entre 0 et 500
        if vie_max >= 0 and vie_max <= 500:
            self._vie_max = vie_max
        # negatif
        elif vie_max < 0:
            self._vie_max = 0
        # plus grand que 500
        elif vie_max > 500:
            self._vie_max = 500


    def subir_degat(self, degat : int) -> None:
        """calcule des dégats subi

        Args:
            degat (int): valeur des dégats
        """
        degat_final = degat - self.armure.points_armure
        #si l'armure ne prend pas tous les dégats
        if degat_final > 0:
            self.vie -= degat_final

    def attaquer(self) -> int:
        """fonction attaquer de base

        Returns:
            int: retourne la valeur de l'attaque
        """
        return self.attaque
    
    def __eq__(self, autre_perso: 'Personnage'):
        """vérifier si 2 personnages sont pareil

        Args:
            autre_perso (Personnage): personnage à comparer

        Returns:
            _type_: vrai si pareil, faux si différent
        """
        if self.nom == autre_perso.nom and self.vie == autre_perso.vie:
            return True
        else:
            return False

    def reset(self) -> None:
        """remettre la vie au max
        """
        self.vie = self.vie_max