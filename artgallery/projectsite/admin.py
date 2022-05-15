from django.contrib import admin
from .models import Art
# Register your models here.
class ArtAdmin(admin.ModelAdmin):
    pass

admin.site.register(Art, ArtAdmin)
