from django.contrib import admin
from .models import Fan, Turi


# @admin.register(Kurs)
# class KursAdmin(admin.ModelAdmin):
#     list_display = ['id']


# @admin.register(Guruh)
# class GuruhAdmin(admin.ModelAdmin):
#     list_display = ['id']

# @admin.register(Oqtuvchi)
# class OqtuvchiAdmin(admin.ModelAdmin):
#     list_display = ['id']


# @admin.register(Dars)
# class DarsAdmin(admin.ModelAdmin):
#     list_display = ['id']

@admin.register(Fan)
class FanAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Turi)
class TuriAdmin(admin.ModelAdmin):
    list_display = ['id']

