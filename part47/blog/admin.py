from django.contrib import admin

# Register your models here.

from .models import ArtikelModel


class ArtikelAdmin(admin.ModelAdmin):
	readonly_fields = [
		'slug','publish','update',
	]

admin.site.register(ArtikelModel,ArtikelAdmin)