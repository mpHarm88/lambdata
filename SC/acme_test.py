"""
Import unit test to perform tests on Product, BoxingGlove, generate_products,
ADJECTIVES, NOUNS 
"""
import unittest
from acme import Product, BoxingGlove
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops"""
    def test_default_product_price(self):
        """Test default product rice being 10"""
        prod = Product("Test Product")
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Testing default product weight 20"""
        prod = Product("Test Product")
        self.assertEqual(prod.weight, 20)

    def test_default_product_flammability(self):
        """Testing default product flammability"""
        prod = Product("Test Product")
        self.assertEqual(prod.flammability, 0.5)


class AcmeBoxingGlove(unittest.TestCase):
    """Testing boxing glove child class"""
    def test_boxing_glove(self):
        """Testing boxing glove explode method"""
        prod = BoxingGlove("Punch")
        self.assertEqual(prod.explode(), "...its a glove")

    def test_boxing_glove_punch(self):
        """Testing boxing glove punch method"""
        prod = BoxingGlove("Punch")
        self.assertEqual(prod.punch(), "Hey that hurt!")


class AcmeReportTest(unittest.TestCase):
    """Testing to see if 30 products are generated"""
    def test_generate_products(self):
        self.assertEqual(len(generate_products()), 30)

    def test_generate_legal_names(self):
        possible = ADJECTIVES + NOUNS
        prod = generate_products()
        name = []
        for x in range(30):
            name.append(prod[x].name)

        self.assertEqual(name, possible)


if __name__ == '__main__':
    unittest.main()
