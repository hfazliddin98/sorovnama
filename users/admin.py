from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Kurs, User

admin.site.unregister(Group)

@admin.register(Kurs)
class KursAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username', 'kurs_id']