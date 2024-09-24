from domain import *
from domain.Inscription import *
from domain.Cours import *
from domain.Session import *


class GroupeCours:

    def __init__(self, cours: Cours, annee, session, enseignant, inscriptions):
        self.cours = cours
        self.annee = annee
        self.session = session
        self.enseignant = enseignant
        if inscriptions:
            self.inscriptions = inscriptions
        else:
            self.inscriptions = []

    def getCours(self):
        return self.cours

    def getAnnee(self):
        return self.annee

    def getSession(self):
        return self.session

    def getEnseignant(self):
        return self.enseignant

    def getInscriptions(self):
        return self.inscriptions

    def getEtudiantsInscrits(self):
        e = []
        for i in self.inscriptions:
            e.append(i.getEtudiant())
        if not e:
            print("Attention Liste etudiant inscrit est vide!")

        return e

    def inscrireEtudiant(self, etud):

        trouve = False
        inscription = None

        # on vérifie que l'étudiant n'est pas déjà inscrit à ce groupeCours
        for ins in self.inscriptions:
            if ins.getEtudiant() == etud:
                trouve = True  # il n'y a aucune opération a effectuer
                print("étudiant déjà inscrit ")
                return ins

        # si ce n'est pas le cas
        if not trouve:
            # on crée une nouvelle inscription
            ins = Inscription(0, False, self, etud)
            self.inscriptions.append(ins)

            # on fait la laison avec Etudiant
            etud.inscrireGroupeCours(self)

        return inscription

    def estInscrit(self, etud):

        if (self.inscriptions):
            for ins in self.inscriptions:
                if (ins.getEtudiant() == etud):
                    return True

        return False

    def desinscrireEtudiant(self, etud):
        if self.estInscrit(self, etud):
            for ins in self.inscriptions:
                if (ins.getEtudiant() == etud):
                    self.inscriptions.remove(ins)
        return self.inscriptions

    def getNoteEtudiant(self, etud):
        if (self.inscriptions):
            for ins in self.inscriptions:
                if (ins.getEtudiant().getCodePermanent().__eq__(etud.getCodePermanent())):
                    return ins.getNoteNumerique()

        return -1

    def setNoteEtudiant(self, etud, note):
        if (self.inscriptions):
            for ins in self.inscriptions:
                if (ins.getEtudiant().getCodePermanent().__eq__(etud.getCodePermanent())):
                    ins.setNoteNumerique(note)

    def getID(self):
        id = ""
        element = self.getCours()
        if isinstance(element, tuple):
            # renvoie le sigle du cours contenu dans un tuple
            id = element[0].getSigle() + "-" + str(self.annee) + \
                "-" + str(self.session.name)
        if isinstance(element, Cours):  # renvoie un Cours, pas un tuple
            id = element.getSigle() + "-" + str(self.annee) + "-" + str(self.session.name)

        return id

    def estInscrit(self, etud):
        if self.inscriptions:
            for inscription in self.inscriptions:
                print(inscription.getEtudiant())
                if inscription.getEtudiant().__eq__(etud):
                    return True
        return False
