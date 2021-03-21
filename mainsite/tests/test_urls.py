from django.test import SimpleTestCase
from mainsite.views import getLandingPage
from django.urls import reverse, resolve

class TestUrls(SimpleTestCase):
    def test_get_landing_page_resolve(self):
        url = reverse('landingpage')
        self.assertEquals(resolve(url).func, getLandingPage)
