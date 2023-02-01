from unicodedata import category
from django.db.models import Q
from django.http import Http404

from apps.other_app.serializers import SlideImgSerializer
from apps.other_app.models import SlideImg

from rest_framework.views import APIView
from rest_framework.response import Response

class SlideImgApi(APIView):
    def get(self, request, format=None):
        slideImg = SlideImg.objects.all()
        serializer = SlideImgSerializer(slideImg, many=True, context={"request": request})
        return Response(serializer.data)