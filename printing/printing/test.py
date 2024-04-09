from django.test import TestCase, Client
from django.urls import reverse
from .models import clients

class ClientsViewsTestCase(TestCase):

    def setUp(self):
        # Create a sample client instance for testing
        self.client = clients.objects.create(
            shop_id=1,
            shop_name="Sample Shop",
            location="Sample Location",
            phone_no=1234567890,
            email="sample@example.com",
            image="https://example.com/sample_image.jpg",
            balance=1000,
            transactions="Sample transactions data",
            amounts="Sample amounts data"
        )

    def test_index_view(self):
        """Test the index view"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customers/index.html')
        self.assertContains(response, "Sample Shop")

    def test_details_of_shop_view(self):
        """Test the details_of_shop view"""
        response = self.client.get(reverse('details_of_shop', args=[self.client.shop_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customers/details.html')
        self.assertContains(response, "Sample Shop")

    def test_shop_list_view(self):
        """Test the shop_list view"""
        response = self.client.get(reverse('shop_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customers/shop_list.html')

    def test_add_transaction_view(self):
        """Test the add_transaction view"""
        response = self.client.get(reverse('add_transaction', args=[self.client.shop_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customers/new-transaction.html')

    def test_delete_shop_view(self):
        """Test the delete_shop view"""
        response = self.client.get(reverse('delete_shop', args=[self.client.shop_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customers/delete-shop.html')

    def test_add_shop_view(self):
        """Test the add_shop view"""
        response = self.client.get(reverse('add_shop'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customers/add-shop.html')

    def test_edit_shop_view(self):
        """Test the edit_shop view"""
        response = self.client.get(reverse('edit_shop', args=[self.client.shop_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customers/edit-shop.html')

    # Write similar test cases for other views as needed
