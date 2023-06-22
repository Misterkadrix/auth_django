from django.db import models

# Create your models here.
# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Member(AbstractUser):
    pass
# (à noter que l’on est bien sur pas obligé d'utiliser AbstractUser mais j’ai juste la flemme)