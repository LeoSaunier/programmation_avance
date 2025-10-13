from django.test import TestCase
from monApp.models import Contenir, Produit, Rayon

class ContenirModelTest(TestCase):
    def setUp(self):
        # Créer un attribut Contenir à utiliser dans les tests
        self.ryn = Rayon.objects.create(nomRayon="RayonPourTest")
        self.prdt = Produit.objects.create(intituleProd="ProduitPourTest",prixUnitaireProd=10.20)
        self.ctnr = Contenir.objects.create(rayon= self.ryn, produit=self.prdt, Qte=20)
    
    def test_Contenir_creation(self):
        self.assertEqual(self.ctnr.Qte, 20)
        self.assertEqual(self.ctnr.produit, self.prdt)
        self.assertEqual(self.ctnr.rayon, self.ryn)
    
    def test_string_representation(self):
        self.assertEqual(str(self.ctnr), "ProduitPourTest dans RayonPourTest (Qte: 20)")
    
    def test_Contenir_updating(self):
        self.ctnr.Qte = 100
        self.ctnr.save()
        # Récupérer l'objet mis à jour
        updated_ctnr = Contenir.objects.get(produit=self.ctnr.produit, rayon=self.ctnr.rayon)
        self.assertEqual(updated_ctnr.Qte, 100)

    def test_Contenir_deletion(self):
        self.ctnr.delete()
        self.assertEqual(Contenir.objects.count(), 0)