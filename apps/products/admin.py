from django.contrib import admin
from apps.products.models import Product, Category, SubCategory

class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 3

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
    fieldsets = (
        (
            None, {
                'fields': ('url_name', 'full_name')
            }
        ),
    )
    inlines = (SubCategoryInline,)



admin.site.register(Category, CategoryAdmin)

class ProductInline(admin.TabularInline):
    model= Product
    extra = 3

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'parent', 'product_count') 
    fieldsets = (
        (
            None, {
                'fields': ('url_name', 'full_name', 'parent')
            }
        ),
    )
    inlines = (ProductInline,)

    def product_count(self, obj):
        return obj.product_set.count()


    def get_ordering(self, request):
        return ('parent', 'url_name')
    

admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product)