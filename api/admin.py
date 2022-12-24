from django.contrib import admin
# Register your models here.
from api.models import Cliente, Cajero, Sucursal, TipoAtencion, Caja, Servicio, Ticket, TicketServicio

admin.site.register(Cliente)
admin.site.register(Cajero)
admin.site.register(Sucursal)
admin.site.register(TipoAtencion)
admin.site.register(Caja)
admin.site.register(Servicio)
admin.site.register(Ticket)
admin.site.register(TicketServicio)