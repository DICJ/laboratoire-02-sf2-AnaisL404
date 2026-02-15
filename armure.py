class Armure:
    """cette classe représente l'armure
    """

    #constructeur
    def __init__(self, nom: str, points_armure: int):
        self.nom = nom 
        
        #initialoisation
        self._points_armure = -1


        self.points_armure = points_armure

    #vérification
    @property
    def points_armure(self) -> int:
        """protection de l'armure

        Returns:
            int: retourne le points d'armure à utiliser
        """
        return self._points_armure
    
    @points_armure.setter
    def points_armure(self, points_armure : int) -> None:
        """valider la protection de l'armure

        Args:
            points_armure (int): protection de l'armure à vérifier
        """
        #entre 0 et 15
        if points_armure >= 0 and points_armure <= 15:
            self._points_armure = points_armure
        # negatif
        elif points_armure < 0:
            self._points_armure = 0
        #plus grand que 15
        elif points_armure > 15:
            self._points_armure = 15