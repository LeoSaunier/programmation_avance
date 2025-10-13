from django.test import TestCase
from monApp.models import Statut
from monApp.forms import StatutForm

class StatutFormTest(TestCase):
    def test_form_valid_data(self):
        form = StatutForm(data = {'libelle': 'StatutPourTest'})
        self.assertTrue(form.is_valid()) # Le formulaire doit être valide

    def test_form_valid_data_too_long(self):
        form = StatutForm(data = {'libelle':
        'StatutPourTestStatutPourTestStatutPourTestStatutPourTestStatutPourTestStatutPourTestStatutPourTestStatutPourTestStatutPourTestStatutPourTestStatutPourTestStatutPourTestStatutPourTestStatutPourTestStatutPourTestStatutPourTestStatutPourTestStatutPourTest'})
        self.assertFalse(form.is_valid()) # Le formulaire doit être invalide
        self.assertIn('libelle', form.errors) # Le champ 'libelle' doit contenir une erreur
        self.assertEqual(form.errors['libelle'], ['Assurez-vous que cette valeur comporte au plus 200 caractères (actuellement 252).'])

    def test_form_valid_data_missed(self):
        form = StatutForm(data = {'libelle': ''})
        self.assertFalse(form.is_valid()) # Le formulaire doit être invalide
        self.assertIn('libelle', form.errors) # Le champ 'libelle' doit contenir une erreur
        self.assertEqual(form.errors['libelle'], ['Ce champ est obligatoire.'])

    def test_form_save(self):
        form = StatutForm(data = {'libelle': 'StatutPourTest'})
        self.assertTrue(form.is_valid())
        stt = form.save()
        self.assertEqual(stt.libelle, 'StatutPourTest')
        self.assertEqual(stt.idStatut, 1)