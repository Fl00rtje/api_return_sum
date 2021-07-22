from rest_framework.test import APIRequestFactory


factory = APIRequestFactory()
request = factory.post('/sum/', {"input": "100 + 4"}, format='json')