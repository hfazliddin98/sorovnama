from django.contrib import admin
from .models import Kurs, Guruh


@admin.register(Kurs)
class KursAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Guruh)
class GuruhAdmin(admin.ModelAdmin):
    list_display = ['id']

