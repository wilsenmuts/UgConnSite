from django.contrib import admin
from .models import Deck, Card, buildhouse, buyhouse, investmoney, buyland, donatemoney, feesandbills, buyitem, others, grieve, article, about,service

def activate(modeladmin, request, queryset):
    queryset.update(is_active=True)
    rows_updated = queryset.update(is_active=True)
    if rows_updated == 1:
        message_bit = '1 deck was'
    else:
        message_bit = '%s decks were' % rows_updated
    modeladmin.message_user(request, "%s marked successfully as active." %message_bit)

activate.short_description='Make Active'


class buildhouseAdmin(admin.ModelAdmin):
    list_display=( 'username', 'reside', 'is_active')
    list_filter =('is_active',)
    search_fields =[ 'reside', 'is_active']
    actions = [activate]

class grieveAdmin(admin.ModelAdmin):
    list_display=['username', 'title', 'about']

# Register your models here.
admin.site.register(Deck)
admin.site.register(about)
admin.site.register(Card)
admin.site.register(buildhouse, buildhouseAdmin)
admin.site.register(buyhouse)
admin.site.register(investmoney)
admin.site.register(buyland)
admin.site.register(donatemoney)
admin.site.register(feesandbills)
admin.site.register(service)
admin.site.register(buyitem)
admin.site.register(others)
admin.site.register(grieve)
admin.site.register(article)