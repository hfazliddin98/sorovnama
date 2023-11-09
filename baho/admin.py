from django.contrib import admin
from .models import Fanlar, Turlar, Oqituvchilar, Umumiy, Sorovnoma ,Baza, Fan, Tur, Oqituvchi


@admin.register(Fan)
class FanAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Tur)
class TurAdmin(admin.ModelAdmin):
    list_display = ['id', 'kurs', 'fan', 'name']

@admin.register(Oqituvchi)
class OqituvchiAdmin(admin.ModelAdmin):
    list_display = ['id', 'kurs', 'fan', 'tur', 'name']

@admin.register(Sorovnoma)
class SorovnomaAdmin(admin.ModelAdmin):
    list_display = ['id', 'umumiy', 'baho', 'baza']

@admin.register(Baza)
class BazaAdmin(admin.ModelAdmin):
    list_display = ['id', 'kurs', 'fan', 'tur', 'oqtuvchi', 'baho']


@admin.register(Fanlar)
class FanlarAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Turlar)
class TurlarAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Oqituvchilar)
class OqituvchilarAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Umumiy)
class UmumiyAdmin(admin.ModelAdmin):
    list_display = ['id', 'fan', 'tur', 'oqituvchi']