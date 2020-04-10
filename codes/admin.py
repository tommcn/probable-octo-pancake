from django.contrib import admin
from .models import classe

# Register your models here.

def publish(ModelAdmin, request, queryset):
    queryset.update(posted=True)
publish.short_description = "Post selected classes"

def unpublish(ModelAdmin, request, queryset):
    queryset.update(posted=False)
unpublish.short_description = "Remove selected classes from site"



@admin.register(classe)
class classeA(admin.ModelAdmin):
    search_fields = ['nom', 'classe_groupe', 'prof', 'commnence', 'fini']
    list_display = ('nom', 'classe_groupe', 'prof', 'commnence', 'code', 'posted')
    list_filter = ('classe_groupe','prof', 'posted')
    actions = [publish, unpublish]

admin.site.site_header = "Interface d'Administration"
