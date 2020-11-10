from django.contrib import admin
from .models import UserProfile

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'default_street_address1',
        'default_street_address2',
        'default_town_or_city',
        'default_county',
        'default_postcode',
        'default_country',
        'is_member',
    )



    ordering = ('user',)




admin.site.register(UserProfile, ProfileAdmin)

