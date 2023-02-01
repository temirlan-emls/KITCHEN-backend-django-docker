from django.db import models
from pytils.translit import slugify



class SlideImg(models.Model):
    slideName = models.CharField('Slide Name', max_length = 255)
    slideSlug = models.SlugField(blank=True)
    slideImage = models.ImageField('Slide Image',upload_to='slide_images')

    def __str__(self):
        return self.slideName

    def save(self, *args, **kwargs):
        self.slug = slugify(self.slideName)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/{self.slideSlug}/'
        