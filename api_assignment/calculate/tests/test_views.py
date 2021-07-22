from rest_framework.test import APIRequestFactory, APITestCase
from ..views import addition


class NumberTestCase(APITestCase):
    def test_response_status_code_1(self):
        """
            Tests the status code with correct input.
        """
        factory = APIRequestFactory()
        request = factory.post('/sum/', {"input": "100 + 4"}, format='json')
        response = addition(request)
        self.assertEqual(response.status_code, 201)

    def test_response_status_code_2(self):
        """
            Tests the status code with incorrect input ("-" instead of "+").
        """
        factory = APIRequestFactory()
        request = factory.post('/sum/', {"input": "100 - 4"}, format='json')
        response = addition(request)
        self.assertEqual(response.status_code, 400)

    def test_response_status_code_3(self):
        """
            Tests the status code with incorrect input (added an "a" to the data).
        """
        factory = APIRequestFactory()
        request = factory.post('/sum/', {"input": "100 + 4a"}, format='json')
        response = addition(request)
        self.assertEqual(response.status_code, 400)