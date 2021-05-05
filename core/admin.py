from django.contrib import admin
from core.models import Evento

# Register your models here.

# Fazer com que apareça a data da tabela junto com o titulo
class EventoAdmin(admin.ModelAdmin):
  list_display = ('titulo', 'data_evento', 'data_criação')
  list_filter = ('titulo', 'data_evento',) # criar um filtro

admin.site.register(Evento, EventoAdmin)
