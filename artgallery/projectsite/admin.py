from django.contrib import admin
from .models import Art
# Register your models here.
class ArtAdmin(admin.ModelAdmin):
    list_display = ("name", "size", "style", "painter", "yearofcreation", "artdescription")
    search_fields = ("name", "painter")

admin.site.register(Art, ArtAdmin)
