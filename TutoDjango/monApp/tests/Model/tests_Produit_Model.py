from django.test import TestCase
from monApp.models import Produit, Categorie, Statut

class ProduitModelTest(TestCase):
    def setUp(self):
        # Créer un attribut produit à utiliser dans les tests
        self.stt = Statut.objects.create(libelle="StatutPourTest")
        self.ctgr = Categorie.objects.create(nomCat="CategoriePourTest")
        self.prdt = Produit.objects.create(intituleProd="ProduitPourTest",prixUnitaireProd=10.20,statut=self.stt, categorie=self.ctgr)
    
    def test_Produit_creation(self):
        self.assertEqual(self.prdt.intituleProd, "ProduitPourTest")
        self.assertEqual(self.prdt.prixUnitaireProd, 10.20)
        self.assertEqual(self.prdt.statut, self.stt)
        self.assertEqual(self.prdt.categorie, self.ctgr)
    
    def test_string_representation(self):
        self.assertEqual(str(self.prdt), "ProduitPourTest")
    
    def test_Produit_updating(self):
        self.prdt.intituleProd = "ProduitPourTests"
        self.prdt.save()
        # Récupérer l'objet mis à jour
        updated_prdt = Produit.objects.get(refProd=self.prdt.refProd)
        self.assertEqual(updated_prdt.intituleProd, "ProduitPourTests")

    def test_Produit_deletion(self):
        self.prdt.delete()
        self.assertEqual(Produit.objects.count(), 0)