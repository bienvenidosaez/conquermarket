from django.contrib import admin
from marketplace.buyers.models import Buyer


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    model = Buyer
    list_display = ('uuid', 'coins', )
