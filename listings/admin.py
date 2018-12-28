from django.contrib import admin
from .models import Listing
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_publish','price','list_date','realtor')
    list_display_links=('id','title')
    list_filter= ('realtor',)
    list_editable=('is_publish',)
    list_per_page=25
    search_fields=('title','price','list_date','realtor')
    



admin.site.register(Listing,ListingAdmin)
