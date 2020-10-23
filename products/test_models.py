from django.test import TestCase
from .models import Product
# Create your tests here.


class TestProductModel(TestCase):

    def test_product_model(self): 
        product = Product.objects.create(product_name='Test Product')
        self.assertEquals(product.product_name,"Test Product")
