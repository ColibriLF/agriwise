from django.contrib import admin
from .models import User, Parcela, Registo

#admin.site.register(User)
#admin.site.register(Parcela)
#admin.site.register(Registo)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')

class RegistoInLine(admin.TabularInline):
    model = Registo
    extra = 1

@admin.register(Parcela)
class ParcelaAdmin(admin.ModelAdmin):
    parcela_display = ('user', 'nome', 'area')
    inlines = [RegistoInLine]
    search_fields = ['parcela__nome']

@admin.register(Registo)
class RegistoAdmin(admin.ModelAdmin):
    registo_display = ('data', 'parcela', 'produto', 'dose')
    search_fields = ['Registo__data', 'Registo__produto']

# Register your models here.
