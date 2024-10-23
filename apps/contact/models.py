from django.db import models

from ckeditor.fields import RichTextField

from apps.common.models import BaseModel


class Contact(BaseModel):
    name = models.CharField(max_length=225, unique=True, null=True, blank=True)
    email = models.EmailField(max_length=225, unique=True, null=True, blank=True) ### max_length defaul holatda 254
    # url = models.URLField(max_length=225, unique=True, null=True, blank=True) ### max_length defaul holatda 200
    message = RichTextField(null=True, blank=True)

    def __str__(self):
        if self.name:
            return f"{self.id}-{self.name}"
        
        return f"{self.id}-{self.email}"
    
    ### if else: bilan yozsam ham bo'lardi
    
    '''
    def __str__(self):
        if self.name:
            return f"{self.id}-{self.name}"
        else:
            return f"{self.id}-{self.email}"
    '''

    '''
    O'zim uchun shu yerda hulosa django frameworkda ishlayotganda if if if... berib oxiriga return berish tezroq va qulay
    '''
