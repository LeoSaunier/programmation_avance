from datetime import date, datetime
from django.test import TestCase
from monApp.models import Produit
from monApp.forms import ProduitForm

class ProduitFormTest(TestCase):
    def test_form_valid_data(self):
        form = ProduitForm(data = {'intituleProd': 'ProduitPourTest','prixUnitaireProd': 10.20, 'date_fabrication': date.today() })
        self.assertTrue(form.is_valid()) # Le formulaire doit être valide

    def test_form_valid_data_too_long(self):
        form = ProduitForm(data = {'intituleProd':
        'ProduitPourTestProduitPourTestProduitPourTestProduitPourTestProduitPourTestProduitPourTestProduitPourTestProduitPourTestProduitPourTestProduitPourTestProduitPourTestProduitPourTestProduitPourTestProduitPourTest' ,'prixUnitaireProd': 10.20, 'date_fabrication': date.today() })
        self.assertFalse(form.is_valid()) # Le formulaire doit être invalide
        self.assertIn('intituleProd', form.errors) # Le champ 'intituleProd' doit contenir une erreur
        self.assertEqual(form.errors['intituleProd'], ['Assurez-vous que cette valeur comporte au plus 200 caractères (actuellement 210).'])

    def test_form_valid_data_missed(self):
        form = ProduitForm(data = {'intituleProd': '','prixUnitaireProd': 10.20, 'date_fabrication': date.today() })
        self.assertFalse(form.is_valid()) # Le formulaire doit être invalide
        self.assertIn('intituleProd', form.errors) # Le champ 'intituleProd' doit contenir une erreur
        self.assertEqual(form.errors['intituleProd'], ['Ce champ est obligatoire.'])

    def test_form_save(self):
        form = ProduitForm(data = {'intituleProd': 'ProduitPourTest','prixUnitaireProd': 10.20, 'date_fabrication': date.today() })
        self.assertTrue(form.is_valid())
        prdt = form.save()
        self.assertEqual(prdt.intituleProd, 'ProduitPourTest')
        self.assertEqual(prdt.refProd, 1)