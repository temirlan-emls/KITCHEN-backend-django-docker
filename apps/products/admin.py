from django.contrib import admin
from apps.products.models import Product, Category, SubCategory
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

admin.site.register(Category)
admin.site.register(SubCategory)

class ProductAdmin(admin.ModelAdmin, DynamicArrayMixin):
    list_display = ('name', 'price') 
    fieldsets = (
        (
            None, {
                'fields': ('name',  'code', 'sub_category', 'price', 'description', 'properties',  'image', 'review', 'isActive')
            }
        ),
    )
    # inlines = (ProductInline,)

    def product_count(self, obj):
        return obj.product_set.count()


    def get_ordering(self, request):
        return ('name',)
    


admin.site.register(Product, ProductAdmin)




# class SubCategoryInline(admin.TabularInline):
#     model = SubCategory
#     extra = 2

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('full_name',)
#     fieldsets = (
#         (
#             None, {
#                 'fields': ('full_name',)
#             }
#         ),
#     )
#     # inlines = (SubCategoryInline,)



# admin.site.register(Category, CategoryAdmin)

# class ProductInline(admin.TabularInline):
#     model= Product
#     extra = 2

# class SubCategoryAdmin(admin.ModelAdmin):
#     list_display = ('full_name', 'product_count') 
#     fieldsets = (
#         (
#             None, {
#                 'fields': ('full_name', 'category')
#             }
#         ),
#     )
#     # inlines = (ProductInline,)

#     def product_count(self, obj):
#         return obj.product_set.count()


#     def get_ordering(self, request):
#         return ('full_name',)
    

# admin.site.register(SubCategory, SubCategoryAdmin)

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price') 
#     fieldsets = (
#         (
#             None, {
#                 'fields': ('name',  'code', 'sub_category', 'price', 'description', 'image', 'image2','image3', 'review','isActive')
#             }
#         ),
#     )
#     # inlines = (ProductInline,)

#     def product_count(self, obj):
#         return obj.product_set.count()


#     def get_ordering(self, request):
#         return ('name',)
    


# admin.site.register(Product, ProductAdmin)

