from django.contrib import admin
from .models import *


class ColorAdmin(admin.TabularInline):
    model = Color
    extra = 0


@admin.register(Product)
class ColorAdmin(admin.ModelAdmin):
    inlines = [ColorAdmin]


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Comment)
admin.site.register(Slide)
admin.site.register(Digikala_Services)
admin.site.register(Guarantees)
admin.site.register(OfferPack)
admin.site.register(News)
