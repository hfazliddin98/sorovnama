from django.contrib import admin
from .models import Fan, Turi, Oqtuvchi, Sorovnoma, Baza


@admin.register(Sorovnoma)
class SorovnomaAdmin(admin.ModelAdmin):
    list_display = ['id', 'oqtuvchi_id', 'baho', 'baza']


@admin.register(Oqtuvchi)
class OqtuvchiAdmin(admin.ModelAdmin):
    list_display = ['id', 'kurs_id', 'fan_id', 'tur_id']

@admin.register(Fan)
class FanAdmin(admin.ModelAdmin):
    list_display = ['id','kurs_id', 'name']


@admin.register(Turi)
class TuriAdmin(admin.ModelAdmin):
    list_display = ['id', 'fan_id', 'name']

@admin.register(Baza)
class BazaAdmin(admin.ModelAdmin):
    list_display = ['id', 'kurs', 'fan', 'tur', 'oqtuvchi', 'baho']

