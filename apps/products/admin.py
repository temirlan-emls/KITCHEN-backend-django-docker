from django.contrib import admin
from apps.products.models import Product, Category, SubCategory
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

class ProductAdmin(admin.ModelAdmin, DynamicArrayMixin):
    list_display = ('name', 'price') 
    fieldsets = (
        (
            None, {
                'fields': ('name',  'code', 'sub_category', 'price', 'description', 'dimensions','consumption', 'properties',  'title_image', 'image', 'image2', 'review', 'isActive')
            }
        ),
    )
    # inlines = (ProductInline,)

    def product_count(self, obj):
        return obj.product_set.count()


    def get_ordering(self, request):
        return ('name',)
    


admin.site.register(Product, ProductAdmin)




class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 2

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    fieldsets = (
        (
            None, {
                'fields': ('category_name','category_image','category_icon',)
            }
        ),
    )
    # inlines = (SubCategoryInline,)



admin.site.register(Category, CategoryAdmin)

class ProductInline(admin.TabularInline):
    model= Product
    extra = 2

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('sub_category_name', 'product_count') 
    fieldsets = (
        (
            None, {
                'fields': ('sub_category_name', 'category', 'sub_category_image', 'sub_category_icon',)
            }
        ),
    )
    # inlines = (ProductInline,)

    def product_count(self, obj):
        print(obj)
        return obj.products.count()


    def get_ordering(self, request):
        return ('sub_category_name',)
    

admin.site.register(SubCategory, SubCategoryAdmin)
