from django.db import models ### default
### uuid
import uuid
### slug
from django.utils.text import slugify
### get_absolute_url
from django.urls import reverse
### ckeditor
from ckeditor.fields import RichTextField
### validator
from django.core.validators import MinValueValidator, MaxValueValidator
## local classes
from apps.user.models import User
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
        return f"{self.id}-{self.name}"  ### obyekt qaytarish berish majburiy har bir modelga
    
    def get_absolute_url(self):
        return reverse('products', kwargs={'slug': self.slug}) ### url nomi va nima bilan borishi
    
    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name) ### oddiy slugify

        ### uuid.uuid4 yoki uuid.uuid5ni integratsiya qilish

        ### self.slug = f"{slugify(self.name)}-{uuid.uuid4()}" ### bu ishlaydi

        ### self.slug = f"{slugify(self.name)}-{uuid.uuid5()}" ### uuid5 integratsiya amalga oshmaydi buni imkoni yo'q

        super().save(*args, **kwargs) ## *yangi hozirgi kunda foydalaniladigan kod

        # super(Category).save(*args, **kwargs) bu eski usul va hozirgi kunda bu kod ishlamaydi lekin oldin ishlagan. Hozirgi kunda bunday qilish mumkin emas

        ### return super().save(*args, **kwargs) bunday qilish umuman hato bunday qilish mumkin emas


class Tag(BaseModel):
    name = models.CharField(max_length=225, unique=True, null=True, blank=True)
    slug = models.SlugField(max_length=225, unique=True, db_index=True, null=True, blank=True)
    image = models.ImageField(upload_to='tag_images/', null=True, blank=True, default='images/default-image.jpg')

    def __str__(self):
        return f"{self.id}-{self.name}"
    
    def get_absolute_url(self):
        return reverse('products', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = f"{slugify(self.name)}-{uuid.uuid4()}" ### uuid4 bilan integratsiya qilindi

        super().save(*args, **kwargs)  ### return bilan berish va super() ichiga class yozish mumkin emas super() o'zi avtomatik oladi eng bosh ota classdan


class Product(BaseModel):

    THE_PRICE = (
        # uzs
        ("UZS", ("UZB")), ### front, back
        # dollar
        ("$", ("USA")),
        # euro
        ("€", ("EURO")),
        # rubl
        ("₽", ("RUS")),
    )

    name = models.CharField(max_length=225, unique=True, null=True, blank=True)
    slug = models.SlugField(max_length=225, unique=True, null=True, blank=True, db_index=True)
    description = RichTextField(null=True, blank=True)
    terms_conditional = models.TextField(null=True, blank=True)
    highlight = RichTextField(blank=True, null=True)
    image_1 = models.ImageField(upload_to="product_images/", null=True, blank=True, default='images/default-image.jpg')
    image_2 = models.ImageField(upload_to="product_images/", null=True, blank=True, default='images/default-image.jpg')
    image_3 = models.ImageField(upload_to="product_images/", null=True, blank=True, default='images/default-image.jpg')
    image_4 = models.ImageField(upload_to="product_images/", null=True, blank=True, default='images/default-image.jpg')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, null=True, blank=True, related_name="product_category")
    tags = models.ManyToManyField(Tag, blank=True, related_name='product_tags')
    author = models.ForeignKey(to="user.User", on_delete=models.CASCADE, null=True, blank=True, related_name="product_author")
    price_type = models.CharField(max_length=225, null=True, blank=True, default=("UZS", ("UZB")), choices=THE_PRICE)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    percentage = models.FloatField(default=0, null=True, blank=True)
    views_count = models.IntegerField(default=0, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = f"{slugify(self.name)}-{uuid.uuid4()}"  ### uuid 4 bilan integratsiya qilindi

        super().save(*args, **kwargs)

    def __str__(self): ### obyekt qaytarish
        return f"{self.id}-{self.name}"


class Review(BaseModel):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True, related_name='user_reviews')
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, null=True, blank=True, related_name="product_reviews")
    review = RichTextField(null=True, blank=True)
    #rating
    rating = models.FloatField( ### IntegerField bilan yozsa ham bo'ladi
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        null=True, blank=True,
        default=0,
    )

    def __str__(self):
        return f"{self.id}-{self.user.get_full_name()}-{self.product.name}-{self.rating}"
    

class Banner(BaseModel):
    image = models.ImageField(upload_to='banners/', null=True, blank=True, default='images/default-image.jpg')
    name = models.CharField(max_length=225, null=True, blank=True, unique=True)
    name_2 = models.CharField(max_length=225, null=True, blank=True, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}-{self.name}-{self.name_2}"
