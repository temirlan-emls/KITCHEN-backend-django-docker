from django_better_admin_arrayfield.models.fields import ArrayField
from io import BytesIO
from PIL import Image
from django.core.files import File

from django.db import models
from pytils.translit import slugify


class Category(models.Model):
    category_name = models.CharField('Category Name',max_length = 150)
    slug = models.SlugField(blank=True)
    category_image = models.ImageField('Category Image',upload_to='category_images', blank=True)
    category_icon = models.ImageField('Category Icon',upload_to='category_icons', blank=True)

        
    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/{self.slug}/'

    class Meta:
        ordering = ('category_name',)

class SubCategory(models.Model):
    sub_category_name = models.CharField('SubCategory Name',max_length = 150)
    slug = models.SlugField(blank=True)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    sub_category_image = models.ImageField('Sub Category Image',upload_to='sub_category_images', blank=True)
    sub_category_icon = models.ImageField('Sub Category Icon',upload_to='sub_category_icons', blank=True)

    def __str__(self):
        return self.sub_category_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.sub_category_name)
        super().save(*args, **kwargs)

    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
    class Meta:
        ordering = ('sub_category_name',)




class Product(models.Model):
    name = models.CharField('Product Name', max_length = 255)
    slug = models.SlugField(blank=True)
    code = models.CharField('Product Code (optional)', max_length = 50, blank=True)
    price = models.IntegerField()
    description = models.TextField('Product Description (optional)', blank=True)
    properties = ArrayField(models.CharField(max_length=100, blank=True, default=''), default=list)
    image = models.ImageField('Product Image',upload_to='products_images')
    review = models.URLField('Product Review (optional)', max_length = 500, default='', blank=True)
    thumbnail = models.ImageField('Thumbnail', upload_to='products_images',  blank=True)
    isActive = models.BooleanField('Is Product Present (optional)', blank=True)
    data_added = models.DateTimeField(auto_now_add=True)
    sub_category = models.ForeignKey(SubCategory, related_name='products', on_delete=models.CASCADE)

    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/{self.sub_category.slug}/{self.slug}/'


    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return ''
        

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)
        return thumbnail

    class Meta:
        ordering = ('-data_added',)