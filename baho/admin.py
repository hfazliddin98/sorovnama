from django.contrib import admin
from .models import Fan, Turi, Oqtuvchi, Sorovnoma


@admin.register(Sorovnoma)
class SorovnomaAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Oqtuvchi)
class OqtuvchiAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(Fan)
class FanAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Turi)
class TuriAdmin(admin.ModelAdmin):
    list_display = ['id']

