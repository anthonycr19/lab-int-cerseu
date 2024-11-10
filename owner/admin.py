from django.contrib import admin

from owner.models import Owner


# Register your models here.
@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais', 'vigente')
    list_filter = ('nombre',)
    search_fields = ('nombre', 'pais')
    #fields = ('pais', 'nombre')
