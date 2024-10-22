from django.db import models

import uuid

from django.utils.text import slugify
from django.urls import reverse

from ckeditor.fields import RichTextField

from apps.common.models import BaseModel

'''
def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})
'''

class Category(BaseModel):
    name = models.CharField(max_length=225, unique=True, null=True, blank=True)
    slug = models.SlugField(max_length=225, unique=True, db_index=True, null=True, blank=True)
    ### default-image berish usuli
    image = models.ImageField(upload_to='category_images/', null=True, blank=True, default='images/default-image.jpg')

    def __str__(self):
        return f"{self.id}-{self.name}"
    
    def get_absolute_url(self):
        return reverse('products', kwargs={'slug': self.slug}) ### url nomi va nima bilan borishi
    
    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)

            ### uuid.uuid4 yoki 5ni integratsiya qilish
            ### self.slug = f"{slugify(self.name)}-{uuid.uuid4()}"
            ### self.slug = f"{slugify(self.name)}-{uuid.uuid5()}"

        super().save(*args, **kwargs) ## yangi hozirgi kunda foydalaniladigan kod

        # super(Category).save(*args, **kwargs) eski usul lekin bunda ham ishlaydi

        ### return super().save(*args, **kwargs) qilish umuman hato bunday qilish mumkin emas 
