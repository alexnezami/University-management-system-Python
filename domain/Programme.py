class Programme:

    def __init__(self, codeProgramme, titre, nombreCredits, cours):
        self.codeProgramme = codeProgramme
        self.titre = titre
        self.nombreCredits = nombreCredits
        if cours:
            self.cours = cours
        else:
            self.cours = []

    # retourne le code du programme
    def getCodeProgramme(self):
        return self.codeProgramme

    # retourne le titre du programme
    def getTitre(self):
        return self.titre

    # retourne le nombre de crédits du programme
    def getNombreCredits(self):
        return self.nombreCredits

    # ajoute un cours à la liste de cours du programme
    def ajouterCours(self, unCours):
        if unCours:
            self.cours.append(unCours)
        else:
            print("Impossible d'ajouter un cours qui n'existe pas")
        return unCours

    # enlève un cours à la liste de cours du programme
    def enleverCours(self, unCours):
        if not self.cours:
            # on vérifie que la liste de cours n'est pas vide
            print("Il n'y a pas de cours dans ce programme")
        else:
            if unCours in self.cours:  # et qu'elle contient le cours
                self.cours.remove(unCours)
        return unCours

    # retourne la liste des cours du programme
    def getCours(self):
        return self.cours
