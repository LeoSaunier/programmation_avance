from django.test import TestCase
from django.urls import reverse
from monApp.models import Statut
from django.contrib.auth.models import User


class StatutCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')
    def test_Statut_create_view_get(self):
        response = self.client.get(reverse('crt-stt')) # Utilisation du nom de l'URL
        self.assertEqual(response.status_code, 200)
        # Tester que la vue de création renvoie le bon template
        self.assertTemplateUsed(response, 'monApp/create_statut.html')
    def test_Statut_create_view_post_valid(self):
        data = { "libelle": "StatutPourTestCreation" }
        response = self.client.post(reverse('crt-stt'), data)
        # Vérifie la redirection après la création
        self.assertEqual(response.status_code, 302)
        # Vérifie qu'un objet a été créé
        self.assertEqual(Statut.objects.count(), 1)
        # Vérifie la valeur de l'objet créé
        self.assertEqual(Statut.objects.last().libelle, 'StatutPourTestCreation')


class StatutDetailViewTest(TestCase):
    def setUp(self):
        self.Statut = Statut.objects.create(libelle="StatutPourTestDetail")
    def test_Statut_detail_view(self):
        response = self.client.get(reverse('dtl_stt', args=[self.Statut.idStatut]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/detail_statut.html')
        # Vérifie que le nom de la Statut est affiché
        self.assertContains(response, 'StatutPourTestDetail')
        # Vérifie que l'id associé est affiché
        self.assertContains(response, '1')


class StatutUpdateViewTest(TestCase):
    def setUp(self):
        self.Statut = Statut.objects.create(libelle="StatutPourTestUpdate")
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')
    def test_Statut_update_view_get(self):
        response = self.client.get(reverse('stt-chng', args=[self.Statut.idStatut]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/update_statut.html')
    def test_update_view_post_valid(self):
        self.assertEqual(self.Statut.libelle, 'StatutPourTestUpdate')
        data = {'libelle': 'StatutPourTestAfterUpdate'}
        response = self.client.post(reverse('stt-chng', args=[self.Statut.idStatut]), data)
        # Redirection après la mise à jour
        self.assertEqual(response.status_code, 302)
        # Recharger l'objet depuis la base de données
        self.Statut.refresh_from_db()
        # Vérifier la mise à jour du nom
        self.assertEqual(self.Statut.libelle, 'StatutPourTestAfterUpdate')


class StatutDeleteViewTest(TestCase):
    def setUp(self):
        self.Statut = Statut.objects.create(libelle="StatutPourTesDelete")
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')
    def test_Statut_delete_view_get(self):
        response = self.client.get(reverse('dlt-stt', args=[self.Statut.idStatut]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/delete_statut.html')
    def test_Statut_delete_view_post(self):
        response = self.client.post(reverse('dlt-stt', args=[self.Statut.idStatut]))
        # Vérifier la redirection après la suppression
        self.assertEqual(response.status_code, 302)
        # Vérifier que l'objet a été supprimé
        self.assertFalse(Statut.objects.filter(idStatut=self.Statut.idStatut).exists())
        # Vérifier que la redirection est vers la liste des catégories
        self.assertRedirects(response, reverse('lst_stts'))