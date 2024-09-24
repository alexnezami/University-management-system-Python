import unittest
from domain.Session import Session
from domain.ServiceDossierAcademique import *


class DATestCreation(unittest.TestCase):

    # setup
    def setup(self):
        print("Tests de création")

    # test de la creation d'un programme
    def testCreationProgramme(self):
        code = "1822"
        titre = "Maitrise en Génie Logiciel"
        mgl = ServiceDossierAcademique.creerProgramme(code, titre, 45)
        self.assertEquals(code, mgl.getCodeProgramme(),
                          "Wrong program code assigned")
        self.assertEquals(titre, mgl.getTitre(), "Wrong title assigned")
        self.assertEquals(mgl, ServiceDossierAcademique.getProgrammeAvecCode(
            code), "Cannot retrieve program by code")

    # test de la creation d'un étudiant
    def testCreationEtudiant(self):
        prenom = "Martin"
        nom = "Bourgeois"
        codePermanent = "BOUM12079901"
        etud = ServiceDossierAcademique.creerEtudiant(
            nom, prenom, codePermanent)
        self.assertEquals(prenom, etud.getPrenom())
        self.assertEquals(nom, etud.getNom())
        self.assertEquals(codePermanent, etud.getCodePermanent())
        self.assertEquals(etud, ServiceDossierAcademique.getEtudiantAvecCodePermanent(codePermanent),
                          "Cannot retrieve student by code permanent")

    # test de la création d'un cours
    def testCreationCours(self):
        sigle = "INF1120"
        titre = "Programmation 1"
        description = "Acquérir une méthode de développement"
        inf1120 = ServiceDossierAcademique.creerCours(
            sigle, titre, description, 3, None)
        self.assertEquals(sigle, inf1120.getSigle(), "Mauvais sigle")
        self.assertEquals(titre, inf1120.getTitre(), "Mauvais titre")
        self.assertEquals(description, inf1120.getDescription(),
                          "Mauvaise description")
        self.assertEquals(inf1120, ServiceDossierAcademique.getCoursAvecSigle(
            sigle), "Ne peut accéder aux cours par sigle")

    # test de la creation d'un groupe cours
    def testCreationGroupeCours(self):
        sigle = "INF1120"
        titre = "Programmation 1"
        description = "Acquérir une méthode de développement"
        inf1120 = ServiceDossierAcademique.creerGroupeCours(
            sigle, titre, description, 3)
        annee = 2023
        session = Session.Session.Automne.value
        professeur = "Tournesol"
        groupeCours = ServiceDossierAcademique.creerGroupeCours(
            inf1120, annee, session, professeur)
        self.assertEquals(inf1120, groupeCours.getCours(),
                          "GroupeCours non associé au bon cours")
        self.assertEquals(annee, groupeCours.getAnnee(),
                          "Groupe cours non associé à la bonne année")
        self.assertEquals(session, groupeCours.getSession(),
                          "Groupe cours associé à la mauvaise session")
        self.assertEquals(professeur, groupeCours.getEnseignant(),
                          "Non attribué au bon professeur")


# permet d'exécuter les classes de test comme un script normal
if __name__ == '__main__':
    unittest.main()
