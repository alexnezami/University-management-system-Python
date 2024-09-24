from domain.Programme import *
from domain.Etudiant import *
from domain.GroupeCours import *
from domain.Cours import *
from domain.Inscription import *


class ServiceDossierAcademique:

    # variables de classe
    listeEtudiants = []
    listeCours = []
    listeGroupesCours = []
    listeProgrammes = []
    listeInscriptions = []

    def __init__(self, listeEtudiants, listeCours, listeGroupesCours, listeProgrammes, listeInscriptions):
        self.listeEtudiants = listeEtudiants
        self.listeCours = listeCours
        self.listeGroupesCours = listeGroupesCours
        self.listeProgrammes = listeProgrammes
        self.listeInscriptions = listeInscriptions

    def creerEtudiant(nom, prenom, codePermanent):
        etudiant = Etudiant.Etudiant(
            nom, prenom, codePermanent, None, 0, 0, None)
        print("Etudiant a été créé")
        ServiceDossierAcademique.listeEtudiants.append(etudiant)
        return etudiant

    def creerProgramme(codeProg, titre, nombreCredits):
        programme = Programme.Programme(codeProg, titre, nombreCredits, None)
        ServiceDossierAcademique.listeProgrammes.append(programme)
        return programme

    def creerCours(sigle, titre, description, nombreCredits, prerequis):
        cours = Cours(sigle, titre, description,
                      nombreCredits, prerequis)
        ServiceDossierAcademique.listeCours.append(cours)
        return cours

    def creerGroupeCours(cours, annee, session, enseignant):
        groupeCours = GroupeCours(
            cours, annee, session, enseignant, None)
        ServiceDossierAcademique.listeGroupesCours.append(groupeCours)
        return groupeCours

    def inscrireEtudiantCours(groupeCours, etudiant):
        inscription = Inscription(0, False, groupeCours, etudiant)
        ServiceDossierAcademique.listeInscriptions.append(inscription)
        return inscription

    def inscrireEtudiantProgramme(etudiant, programme):
        etudiant.inscrireProgramme(programme)
        return etudiant

    def saisirNote(etudiant, groupeCours, note):
        for i in ServiceDossierAcademique.listeInscriptions:
            if i.getEtudiant() == etudiant and i.getGroupeCours() == groupeCours:
                etudiant.setNoteGroupeCours(groupeCours, note)

    def getMoyenne(etudiant):
        return etudiant.getMoyenneCumulative()

    def getNombreCreditsCompletes(etudiant):
        return etudiant.getNombreCreditsReussis()

    def getEtudiantAvecCodePermanent(codePerment):
        trouve = False
        if ServiceDossierAcademique.listeEtudiants:
            for etudiant in ServiceDossierAcademique.listeEtudiants:
                print("Etudiant = ")
                print(etudiant)
                if etudiant.getCodePermanent().__eq__(codePerment):
                    trouve = True
                    return etudiant
        if not ServiceDossierAcademique.listeEtudiants:
            print("La liste d'étudiants est vide")
            return None
        if not trouve:
            return None

    def getCoursAvecSigle(sigle):
        trouve = False
        for cours in ServiceDossierAcademique.listeCours:
            if cours.getSigle().__eq__(sigle):
                trouve = True
                return cours
        if not trouve:
            return None

    def getProgrammeAvecCode(codeProgramme):
        trouve = False
        for programme in ServiceDossierAcademique.listeProgrammes:
            if programme.getCodeProgramme().__eq__(codeProgramme):
                trouve = True
                return programme
        if not trouve:
            return None

    def getGroupeCoursAvecCode(codeGroupeCours):
        trouve = False
        for groupeCours in ServiceDossierAcademique.listeGroupesCours:
            if groupeCours.getID().__eq__(codeGroupeCours):
                trouve = True
                return groupeCours
        if not trouve:
            return None
