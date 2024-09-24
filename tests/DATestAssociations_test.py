import unittest
from domain import Session
from domain.ServiceDossierAcademique import *


class DATestAssociations(unittest.TestCase):

    # setup
    def setUp(self):
        # création des cours
        inf1120 = ServiceDossierAcademique.creerCours("INF1120", "Programmation 1",
                                                      "Acquérir une méthode de développement", 3, None),
        inf2120 = ServiceDossierAcademique.creerCours("INF2120", "Programmation II",
                                                      "Approfondir les concepts de la programmation OO", 3, inf1120)
        inf3135 = ServiceDossierAcademique.creerCours("INF3135", "Construction et maintenance de logiciels",
                                                      "Initier les étudiants à la programmation à l’aide d’un langage impératif et procédural.",
                                                      3, inf1120)
        inf5151 = ServiceDossierAcademique.creerCours("INF5151", "Génie logiciel: analyse et modélisation",
                                                      "Explorer les fondements et l’évolution des méthodes d’analyse", 3, None)
        inf5153 = ServiceDossierAcademique.creerCours("INF5153", "Génie logiciel: conception",
                                                      "Sensibiliser l’étudiant aux difficultés de la conception", 3,
                                                      inf3135)

        # création des groupes cours
        inf1120_aut_2020 = ServiceDossierAcademique.creerGroupeCours(
            inf1120, 2020, Session.Session.Automne, None)
        inf5151_hiv_2022 = ServiceDossierAcademique.creerGroupeCours(
            inf5151, 2022, Session.Session.Hiver, None)
        inf1120_aut_2021 = ServiceDossierAcademique.creerGroupeCours(
            inf1120, 2021, Session.Session.Automne, None)
        inf2120_hiv_2021 = ServiceDossierAcademique.creerGroupeCours(
            inf2120, 2021, Session.Session.Hiver, None)
        inf2120_hiv_2022 = ServiceDossierAcademique.creerGroupeCours(
            inf2120, 2022, Session.Session.Hiver, None)
        inf3135_aut_2021 = ServiceDossierAcademique.creerGroupeCours(
            inf3135, 2021, Session.Session.Automne, None)
        inf5153_aut_2022 = ServiceDossierAcademique.creerGroupeCours(
            inf5153, 2022, Session.Session.Automne, None)

        # création des étudiants
        martin = ServiceDossierAcademique.creerEtudiant(
            "Martin", "Bourgeois", "BOUM12079901")
        josee = ServiceDossierAcademique.creerEtudiant(
            "Josée", "Cyr", "CYRJ05530301")

        # création des inscriptions
        inscription = None

        # martin. On essaie les deux façons d'inscrire martin, via:
        # 1) classe Etudiant
        inscription = martin.inscrireGroupeCours(
            inf1120_aut_2020)
        # 2) classe GroupeCours
        inscription = inf2120_hiv_2021.inscrireEtudiant(martin)  # ou de là ?
        inscription = martin.inscrireGroupeCours(inf3135_aut_2021)
        inscription = martin.inscrireGroupeCours(inf5151_hiv_2022)
        inscription = martin.inscrireGroupeCours(inf5153_aut_2022)

        inscription = josee.inscrireGroupeCours(inf1120_aut_2021)
        inscription = inf2120_hiv_2022.inscrireEtudiant(josee)

    # tear down

    def tearDown(self):
        print("fin du test")

    # test le lien entre un programme et un cours
    def testLienProgrammeCours(self):
        code = "1822"
        titre = "Maitrise en Génie Logiciel"
        mgl = ServiceDossierAcademique.creerProgramme(code, titre, 45)
        mgl7260 = ServiceDossierAcademique.creerCours("MGL7260", "Exigences et spécifications de systèmes logiciels",
                                                      "Introduction à l'ingénierie des systèmes. - Modèles de processus des exigences logicielles",
                                                      3, None)
        mgl7361 = ServiceDossierAcademique.creerCours("MGL7361",
                                                      "Principes et applications de la conception de logiciels",
                                                      "Rôle de la conception dans le cycle de vie du logiciel", 3, mgl7260)
        mgl7460 = ServiceDossierAcademique.creerCours("MGL7460", "Réalisation et maintenance de logiciels",
                                                      "Rôle de la réalisation et de la maintenance dans le cycle de vie du logiciel",
                                                      3, mgl7361)
        mgl.ajouterCours(mgl7260)
        mgl.ajouterCours(mgl7361)
        mgl.ajouterCours(mgl7460)

        found = False

        listeCoursMGL = mgl.getCours()
        for c in listeCoursMGL:
            found = c.__eq__(mgl7361) or found

        self.assertTrue(
            found, "On ne trouve pas un cours qui a été ajouté au programme")

    # test du lien entre étudiant et inscription
    def testLienEtudiantInscriptionGroupeCours(self):
        martin = ServiceDossierAcademique.getEtudiantAvecCodePermanent(
            "BOUM12079901")
        self.assertTrue(ServiceDossierAcademique.getGroupeCoursAvecCode("INF1120-2020-Automne").estInscrit(martin),
                        "Martin n'a pas été inscrit")
        self.assertTrue(ServiceDossierAcademique.getGroupeCoursAvecCode("INF2120-2021-Hiver").estInscrit(martin),
                        "Martin n'a pas été inscrit")

    # test de l'attribution de notes
    def testAttributionNotes(self):
        martin = ServiceDossierAcademique.getEtudiantAvecCodePermanent(
            "BOUM12079901")

        self.assertIsNotNone(martin)

        # attribuer les notes de martin
        martin.setNoteGroupeCours(ServiceDossierAcademique.getGroupeCoursAvecCode(
            "INF1120-2020-Automne"), float(3.3))
        martin.setNoteGroupeCours(ServiceDossierAcademique.getGroupeCoursAvecCode(
            "INF2120-2021-Hiver"), float(3.7))
        # tester l'accès aux notes via martin ...
        self.assertEquals(float(3.3), martin.getNotePourCours(ServiceDossierAcademique.getCoursAvecSigle("INF1120")),
                          "Ouains, la note de martin est erronée")
        # et via le groupe cours
        self.assertEquals(float(0),
                          ServiceDossierAcademique.getGroupeCoursAvecCode(
                              "INF2120-2021-Hiver").getNoteEtudiant(martin),
                          "Ouains, pas fort ton système")

        # nettoyer pour pas que ça pollue les autres tests
        martin.setNoteGroupeCours(ServiceDossierAcademique.getGroupeCoursAvecCode(
            "INF1120-2020-Automne"), float(0.0))
        martin.setNoteGroupeCours(ServiceDossierAcademique.getGroupeCoursAvecCode(
            "INF2120-2021-Hiver"), float(0.0))

    # test de la moyenne cumulative
    def testMoyenneCumulative(self):
        martin = ServiceDossierAcademique.getEtudiantAvecCodePermanent(
            "BOUM12079901")
        josee = ServiceDossierAcademique.getEtudiantAvecCodePermanent(
            "CYRJ05530301")

        # attribuer les notes de martin
        martin.setNoteGroupeCours(ServiceDossierAcademique.getGroupeCoursAvecCode(
            "INF1120-2020-Automne"),  float(3.3))
        martin.setNoteGroupeCours(ServiceDossierAcademique.getGroupeCoursAvecCode(
            "INF2120-2021-Hiver"),  float(3.7))
        martin.setNoteGroupeCours(ServiceDossierAcademique.getGroupeCoursAvecCode(
            "INF3135-2021-Automne"),  float(2.7))
        martin.setNoteGroupeCours(ServiceDossierAcademique.getGroupeCoursAvecCode(
            "INF5151-2022-Hiver"),  float(4.0))

        # verifier que josee est inscrite au cours en question
        self.assertTrue(ServiceDossierAcademique.getGroupeCoursAvecCode("INF1120-2021-Automne").estInscrit(josee),
                        "Oops! josée n'est pas inscrite dans le INF1120-2021-Automne")
        # attribuer les notes de josee
        josee.setNoteGroupeCours(ServiceDossierAcademique.getGroupeCoursAvecCode(
            "INF1120-2021-Automne"),  float(4.3))
        josee.setNoteGroupeCours(ServiceDossierAcademique.getGroupeCoursAvecCode(
            "INF2120-2022-Hiver"),  float(4.3))

        # tester moyenne cumulative de martin
        self.assertEquals(float(3.425), martin.getMoyenneCumulative(),
                          "Moyenne cumulative de martin mal calculee")
        # test moyenne cumulative de josee
        self.assertEquals(float(4.3), josee.getMoyenneCumulative(),
                          "Moyenne cumulative de josee mal calculee")


# permet d'exécuter les classes de test comme un script normal
if __name__ == '__main__':
    unittest.main()
