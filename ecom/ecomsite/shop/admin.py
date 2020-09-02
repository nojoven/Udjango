from django.contrib import admin
from .models import Products
from .models import Order


# Register your models here.
admin.site.site_header = "E-commerce-Site"
admin.site.site_title = "Manage ABC "
admin.site.index_title = "Welcome Admin!"


class ProductAdmin(admin.ModelAdmin):
    
    def change_category_to_default(self, request, queryset):
        queryset.update(category="default")

    change_category_to_default.short_description = 'Default Category'
    list_display = ('title', 'price', 'discount_price', 'category', 'description', 'image')
    search_fields = ('category',)
    # search_fields = ('title',) the filter must be a tuple
    # search_fields = ('title',)

    actions = ('change_category_to_default',)

    # Now we show only the title and the price of the article on the admin page of this article
    fields = ('title', 'price',)

    # Allows the admin to easily update specific fields
    list_editable = ('price', 'description',)


admin.site.register(Products, ProductAdmin)
admin.site.register(Order)
