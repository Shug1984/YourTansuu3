from django.contrib import admin
from .models import (Item, Closet, ItemType, ItemColor, ItemBrand, PurchasePlace)

admin.site.register(Item)
admin.site.register(Closet)
admin.site.register(ItemType)
admin.site.register(ItemColor)
admin.site.register(ItemBrand)
admin.site.register(PurchasePlace)


# Register your models here.
