class Cours:

    def __init__(self, sigle, titre, description, nombreCredits, prerequis):
        self.sigle = sigle
        self.titre = titre
        self.description = description
        self.nombreCredits = nombreCredits
        self.prerequis = prerequis

    # retourne le sigle du cours
    def getSigle(self):
        return self.sigle

    # retourne le titre du cours
    def getTitre(self):
        return self.titre

    # retourne la description du cours
    def getDescription(self):
        return self.description

    # retourne le nombre de credits du cours
    def getNombreCredits(self):
        return self.nombreCredits

    # retourne les prerequis du cours
    def getPrerequis(self):
        return self.prerequis

    # ajoute un prerequis pour le cours
    def ajouterPrerequis(self, prerequis):
        if (self.prerequis.add(prerequis)):
            return prerequis
        else:
            return None

    # retirer un prérequis au cours
    def retirerPrerequis(self, prerequis):
        if (self.prerequis.remove(prerequis)):
            return prerequis
        else:
            return None
