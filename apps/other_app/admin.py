from django.contrib import admin
from apps.other_app.models import SlideImg

class SlideImgAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None, {
                'fields': ('slideName',  'slideImage')
            }
        ),
    )


    def get_ordering(self, request):
        return ('slideName',)
    
admin.site.register(SlideImg, SlideImgAdmin)