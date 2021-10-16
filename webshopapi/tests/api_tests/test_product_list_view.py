from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from webshopapi.models import ProductModel


class TestProductsListView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        ProductModel.objects.create(name="Lego bricks", price=5.55)

    def test__products_list_api__success(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('products_list_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0].get('name'), "Lego bricks")

