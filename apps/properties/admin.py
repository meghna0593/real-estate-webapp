from django.contrib import admin
from .models import Property, PropertyPhoto, PropertyViews


class PropertyPhotoInline(admin.TabularInline):
    model = PropertyPhoto
    extra = 1


class PropertyAdmin(admin.ModelAdmin):
    list_display = ["title", "country", "advert_type", "property_type"]
    list_filter = ["advert_type", "property_type", "country"]
    inlines = [PropertyPhotoInline]


admin.site.register(Property, PropertyAdmin)
admin.site.register(PropertyPhoto)
admin.site.register(PropertyViews)
