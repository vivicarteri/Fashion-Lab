from django.contrib import admin
from .models import Usuario
from .models import Partes_de_Cima
from .models import Partes_de_Baixo
from .models import Calçados
from .models import Acessórios

admin.site.register(Partes_de_Cima)
admin.site.register(Partes_de_Baixo)
admin.site.register(Calçados)
admin.site.register(Acessórios)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'nome', 'genero', 'cpf', 'data_nascimento') 
    search_fields = ('user__username', 'nome', 'cpf') 

admin.site.register(Usuario, UsuarioAdmin)