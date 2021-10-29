from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.models import User
from api.serializers import UserSerializer
# Also add these imports
from api.permissions import IsLoggedInUserOrAdmin, IsAdminUser

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib import messages
from django.core.mail import EmailMessage
from django.http import request


def index(request):
   
    return render(request,'api/index.html' )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # email= EmailMessage(' SUBJECT' ,
    #                      'CONGRATULATIONS! YOU MADE IT TO THE ADMIN',
    #                     to=['tpart392@gmail.com'],
    #                    # headers={'Reply-To':User.email},
    #                     )
    # email.send()
    # messages.success(request,'Email Succesfully submitted')

    # from django.core.mail import send_mail
# send_mail(
#     'Subject here',
#     'Here is the message.',
#     'tpart392@gmail.com',
#     ['thennyswhyte@example.com'],
#     fail_silently=False,
# )

    # PERMISSINS FOR USERS TO DESTROY OR UPDATE THEIR OWN RECORDS
    # PERMISSIONS FOR SUPER ADMIN USERS CREATE USERS
    # CRUD DJANGO DEFAULT (CREATE RETRIEVE UPDATE DESTROY)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
