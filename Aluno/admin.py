from django.contrib import admin

# Register your models here.
from Aluno.models import aluno


# Register your models here.
@admin.register(aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'curso', 'email']