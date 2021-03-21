from typing import Collection
from django.test import TestCase, Client
from django.urls import reverse
from mainsite.views import getLandingPage
import json

# class TestViews(TestCase):
#     def test_get_landing_page_view_GET(self):
#         client = Client()
#         response = client.get(reverse('landingpage'))
        
        
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'mainsite/index.html')