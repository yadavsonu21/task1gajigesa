from django.test import TestCase, Client
from rest_framework import  status
from rest_framework.test import APITestCase
# test case for testing api endpoint as of now only one path is created console printing will give as result
class MyAPITestCase(APITestCase):
    def setUp(self):
        self.client = Client()

    def test_api_response(self):
        url = ''
        data = {'input':'How are you'}
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        print(response.content)
        # self.assertTrue('result' in response)
        # self.assertEqual(response.data['result'],'success')

# to run this > python manage.py test base.test_views