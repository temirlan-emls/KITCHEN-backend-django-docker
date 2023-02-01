from rest_framework import serializers
from apps import other_app
from apps.other_app.models import SlideImg
from django.conf import settings

class SlideImgSerializer(serializers.ModelSerializer):
    slide_image_url = serializers.SerializerMethodField()


    class Meta: 
        model = SlideImg 
        fields = (
            'id',
            'slideName',
            'slideSlug',
            'slide_image_url',
        )
        


    def get_slide_image_url(self, SlideImg):
        if SlideImg.slideImage == '':
            return None
        else:
            request = self.context.get('request')
            photo_url = SlideImg.slideImage.url
            return request.build_absolute_uri(photo_url)
