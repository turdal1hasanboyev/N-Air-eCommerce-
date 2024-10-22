from django.db import models

from apps.common.models import BaseModel

from django.contrib.auth.models import AbstractUser


class User(AbstractUser, BaseModel):
    pass
