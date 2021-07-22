from rest_framework.test import APITestCase
from ..models import Number


class NumberTest(APITestCase):
    """
        Test module for the Number model.
    """

    def setUp(self):
        set1 = Number.objects.create(num_1=10, num_2=100)
        set2 = Number.objects.create(num_1=20, num_2=200)

    def test_number_num_1(self):
        set_1 = Number.objects.get(num_2=100)
        set_2 = Number.objects.get(num_2=200)

        self.assertEqual(
            set_1.num_1, 10)
        self.assertEqual(
            set_2.num_1, 20)

    def test_number_num_2(self):
        set_1 = Number.objects.get(num_1=10)
        set_2 = Number.objects.get(num_1=20)

        self.assertEqual(
            set_1.num_2, 100)
        self.assertEqual(
            set_2.num_2, 200)