from domain import *
class Inscription:


    def __init__(self, noteNumerique, reussi,  groupeCours, etudiant):
        self.noteNumerique = noteNumerique
        self.reussi = reussi
        self.groupeCours = groupeCours
        self.etudiant = etudiant


    def getNoteNumerique(self):
        return self.noteNumerique
    
    def isReussi(self):
        return self.reussi
    
    def getEtudiant(self):
        return self.etudiant
    
    def getGroupeCours(self):
        return self.groupeCours
    
    def setNoteNumerique(self, note):
        self.noteNumerique=note