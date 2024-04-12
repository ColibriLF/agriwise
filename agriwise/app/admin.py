from django.contrib import admin
from .models import User, List, Item

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')

class ItemInline(admin.TabularInline):
    model = Item
    extra = 1

@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')
    inlines = [ItemInline]

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'list', 'done', 'created_at')
