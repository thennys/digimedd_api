from django.test import TestCase

# Create your tests here.
from django.http import response
from django.test import TestCase
from api.views import *
# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse


# # class UserViewSet_api_test(APITestCase):
# #     def test_UserViewSet(self):
# #         response = self.client.get('/api/auth/login')
# #         self.assertEqual(response.status_code, status.HTTP_200_OK)


# class UserViewSet_api_test(APITestCase):
#     def setUp(self):
#         self.superuser = User.objects.create_superuser('john', 'ssd@gmail.com', 'johnpassword')
#         self.client.login(username='john', password='dennis1234')
#         self.data = {'username': 'ssd@gmail.com', 'first_name': 'Mike', 'last_name': 'Tyson'}

#     def test_UserViewSet(self):
#         response = self.client.post(reverse('user-list'), self.data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)


from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase

from .views import *


class UserViewSet_api_test(APITestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='tpart392@gmail.com', email='tpart392@.com', password='juniors.')

    def test_UserViewSet(self):
        # Create an instance of a GET request.
        request = self.factory.get('/api/auth/login')

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        request.user = self.user

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()

        
        response = UserViewSet_api_test(request),
        # Use this syntax for class-based views.
        response = UserViewSet_api_test.as_view()(request)
        self.assertEqual(response.status_code, 200)
