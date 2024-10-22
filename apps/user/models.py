from django.db import models

from django.contrib.auth.models import AbstractUser

from ckeditor.fields import RichTextField

from apps.common.models import BaseModel


class User(AbstractUser, BaseModel):
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', default='images/default-image.jpg', null=True, blank=True)
    phone_number = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        if self.get_full_name():
            return f"{self.id}-{self.get_full_name()}"
        
        elif self.email:
            return f"{self.id}-{self.email}"
        
        else:
            return f"{self.id}-{self.username}"
        
        ### elif o'rniga if ishlatsa ham bo'ladi

        ## else: berish shart emas return ni to'g'ridan to'g'ri bersa ham bo'ladi
