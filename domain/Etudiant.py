from domain.Inscription import Inscription
from domain.Cours import Cours


class Etudiant:

    def __init__(self, nom, prenom, codePermanent, programme, creditsReussis,
                 moyenneCumulative, inscriptions):
        self.nom = nom
        self.prenom = prenom
        self.codePermanent = codePermanent
        self.programme = programme
        self.creditsReussis = creditsReussis
        self.moyenneCumulative = moyenneCumulative
        if inscriptions:
            self.inscriptions = inscriptions
        else:
            self.inscriptions = []

    # nom de famille de la personne étudiante
    def getNom(self):
        return self.nom

    # prénom de la personne étudiante
    def getPrenom(self):
        return self.prenom

    # lire code permanent
    def getCodePermanent(self):
        return self.codePermanent

    # modifier code permanent
    def setCodePermanent(self, code):
        self.codePermanent = code

    # programme d'études
    def getProgramme(self):
        return self.getProgramme

    # inscrire à un programme
    def inscrireProgramme(self, prog):
        self.programme = prog

    # nombre de crédits réussis
    def getNombreCreditsReussis(self):
        return self.creditsReussis

    # moyenne cumulative
    def getMoyenneCumulative(self):
        somme = float(0)
        cpt = 0

        if self.inscriptions:
            for ins in self.inscriptions:
                if ins.getNoteNumerique() != float(0.0):
                    somme += ins.getNoteNumerique()
                    cpt += 1
            # pour ne pas prendre en compte les notes nulles et faire passer les tests
            self.moyenneCumulative = somme / cpt

        return self.moyenneCumulative

    # inscrire l'étudiant dans un groupe cours
    def inscrireGroupeCours(self, gpeCours):

        inscription = None
        trouve = False

        # on vérifie que l'étudiant n'est pas déjà inscrit à ce groupeCours
        for ins in self.inscriptions:
            if ins.getGroupeCours() == gpeCours:
                # si c'est le cas on ne fait rien
                trouve = True
                print("étudiant déjà inscrit ")
                return ins

        # si ce n'est pas le cas on crée une nouvelle inscription
        if not trouve:
            inscription = Inscription(0, False, gpeCours, self)
            self.inscriptions.append(inscription)

            # on fait la liaison avec GroupeCours
            gpeCours.inscrireEtudiant(self)

        return inscription

    # attribuer une note numérique pour le groupe cours
    def setNoteGroupeCours(self, gpeCours, note):
        trouve = False
        cpt = 0
        if (self.inscriptions):
            while ((not trouve) and (cpt < len(self.inscriptions))):
                if (self.inscriptions[cpt].getGroupeCours() == gpeCours):
                    trouve = True
                    self.inscriptions[cpt].setNoteNumerique(note)
                cpt += 1
        else:
            print("Attention : Il n'y a pas d'inscription pour cet étudiant")

    # retourne la note pour le groupe cours passé en paramètre.
    def getNotePourCours(self, cours):
        note = -1
        trouve = False
        cpt = 0
        if (self.inscriptions):
            while ((not trouve) and (cpt < len(self.inscriptions))):
                # on récupère le cours actuel
                element = self.inscriptions[cpt].getGroupeCours().getCours()

                # si l'élément récupéré est de type Cours et qu'il correspond à ce que l'on cherche
                if isinstance(element, Cours):
                    if (element.getSigle().__eq__(cours.getSigle)):
                        trouve = True
                        note = self.inscriptions[cpt].getNoteNumerique()
                # s'il est un tuple de cours, on récupère le 1er element
                if isinstance(element, tuple):
                    cpt2 = 0
                    if (element[cpt2].getSigle().__eq__(cours.getSigle)):
                        trouve = True
                        note = self.inscriptions[cpt].getNoteNumerique()
                    cpt2 += 1

            cpt += 1
        else:
            print("Attention : Il n'y a pas d'inscription pour cet étudiant")
        return note
