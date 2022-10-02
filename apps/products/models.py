from email.policy import default
from pydoc import describe
from django.db import models
from apps.products.managers import CategoryManager, SubCategoryManager

class Node(models.Model):
    full_name = models.CharField('Full Name',max_length = 150)
    url_name = models.CharField('URL Name',max_length = 100)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name = 'children',
        null = True,
        blank = True
    )

    def __str__(self):
        return self.full_name
    
    class Meta:
        ordering = ('url_name'),
        verbose_name_plural = 'Nodes'

class Category(Node):
    objects = CategoryManager()

    class Meta:
        proxy = True
        verbose_name_plural = 'Categories'

class SubCategory(Node):
    objects = SubCategoryManager()
    class Meta:
        proxy = True
        verbose_name_plural = 'Sub Categories'


class Product(models.Model):
    name = models.CharField('Product Name', max_length = 200)
    code = models.CharField('Product Code', max_length = 50, default='')
    price = models.IntegerField(default=0)
    description = models.TextField('Product Description', blank=True)
    image = models.ImageField(upload_to='products_images')
    review = models.URLField('Product Review', max_length = 500, default='', blank=True)
    isActive = models.BooleanField(blank=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name