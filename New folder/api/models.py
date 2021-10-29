from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.utils import timezone
# Create your models here.

# CUSTOM USER MODELSS


class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=233)
    email = models.EmailField(_('email address'), unique=True)

# THIS WILL ALLOW USERS TO LOGIN IN WITH EMAILS AS USERNAMES
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)


PROGRAMMING_LANGUAGES = (
    ("PYTHON", "DJANGO"),
    ("REST", "FRAMEWORKS"),
    ("CSS", "HTML"),
    ("JAVA", "JAVASCRIPT"),
)
DEVLOPPER_ROLE = (
    ("FRONTEND", "BACKEND"),
    ("API_BUILDER", "UI-DESIGNER"),
    ("PROJECT-MANAGEMENT", "MOBILE_DEVELOPPER"),
    ("ANDRIOD-DEVELOPPER", "IOS DEVELOPPER"),
)


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='records')
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    date_employed = models.DateTimeField(default=timezone.now)
    developer_role = models.CharField(
        choices=DEVLOPPER_ROLE, default='BACKEND', max_length=100, null=True)
    programming_language = models.CharField(max_length=9,
                                            choices=PROGRAMMING_LANGUAGES,
                                            default="PYTHON", null=True)

    userid = models.CharField(
        max_length=8, default='AB-12345', blank=False, unique=True)
    photo = models.ImageField(upload_to='uploads', blank=True)

    class Meta:
        ordering = ['email']
        db_table = ''
        managed = True
