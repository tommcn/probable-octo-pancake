from django.contrib import admin
from .models import classe

# Register your models here.
@admin.register(classe)
class classeA(admin.ModelAdmin):
    search_fields = ['nom', 'classe_groupe', 'prof', 'commnence', 'fini']
    list_display = ('nom', 'classe_groupe', 'prof', 'commnence', 'code')
    list_filter = ('classe_groupe','prof')

admin.site.site_header = "Interface d'Administration"
