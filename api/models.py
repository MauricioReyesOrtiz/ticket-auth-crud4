from django.db import models 
import datetime


# Crea tu modelo aquí

#---Cliente----------------------------------------------------------------------------------------
class Cliente(models.Model):
    clienteName = models.CharField(max_length=200)
    clientePaterno = models.CharField(max_length=200)
    clienteMaterno = models.CharField(max_length=200)
    clienteFechanac = models.DateField(null=True)
    clienteTelefono = models.CharField(max_length=200)
    fotocliente = models.ImageField(null=True, blank=True, upload_to='fotos/')
    #productoDescription = models.CharField(blank=True, max_length=200)
    #productoPrice = models.DecimalField(max_digits=10, decimal_places=2)
    #productoImage = models.ImageField(null=True, blank=True, upload_to='images/')
    # create_at = models.DateTimeField(default=datetime.datetime.now)
    
    def cliente_completo(self):
        return "{} {} {}".format(self.clienteName, self.clientePaterno, self.clienteMaterno)
    
    def __str__(self):
        return self.cliente_completo()
    
    #def __str__ (self):
    #    return self.clienteName
    
    
#---Cajero----------------------------------------------------------------------------------------
class Cajero(models.Model):
    nombreCajero = models.CharField('Nombre', max_length = 100)
    paterno = models.CharField('Paterno', max_length = 200)
    materno = models.CharField('Materno', max_length = 200)
    Fechanac = models.DateField()
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    #foto = models.ImageField(null=True, blank=True, upload_to='fotos/')
    #Fechanac = models.DateTimeField(default=datetime.datetime.now)
    
    def cajero_completo(self):
        return "{} {} {}".format(self.nombreCajero, self.paterno, self.materno)
    
    def __str__(self):
        return self.cajero_completo()
    
    
    #def __str__ (self):
     #   return self.nombreCajero


#---Sucursal----------------------------------------------------------------------------------------
class Sucursal(models.Model):
    sucursalNombre = models.CharField(max_length=200)
    sucursalCiudad = models.CharField(max_length=200,null=True)
    sucursalDireccion = models.CharField(max_length=200)
    sucursalHorario = models.CharField(max_length=200)
    #productoDescription = models.CharField(blank=True, max_length=200)
    #productoPrice = models.DecimalField(max_digits=10, decimal_places=2)
    #productoImage = models.ImageField(null=True, blank=True, upload_to='images/')
    # create_at = models.DateTimeField(default=datetime.datetime.now)
    
    def sucursal_completo(self):
        return "{}-{}".format(self.sucursalNombre, self.sucursalCiudad)
    
    def __str__(self):
        return self.sucursal_completo()
    
    #def __str__ (self):
     #   return self.sucursalNombre
    
    
#---TipoAtencion----------------------------------------------------------------------------------------
class TipoAtencion(models.Model):
    atencionNombre = models.CharField(max_length=200)
    #productoDescription = models.CharField(blank=True, max_length=200)
    #productoPrice = models.DecimalField(max_digits=10, decimal_places=2)
    #productoImage = models.ImageField(null=True, blank=True, upload_to='images/')
    # create_at = models.DateTimeField(default=datetime.datetime.now)
    def __str__ (self):
        return self.atencionNombre


#---Caja------------------------------------------------------------------------------------------------
class Caja(models.Model):
    cajaNombre = models.CharField(max_length=200)
    #productoDescription = models.CharField(blank=True, max_length=200)
    #productoPrice = models.DecimalField(max_digits=10, decimal_places=2)
    #productoImage = models.ImageField(null=True, blank=True, upload_to='images/')
    # create_at = models.DateTimeField(default=datetime.datetime.now)
    def __str__ (self):
        return self.cajaNombre


#---Servicio------------------------------------------------------------------------------------------------
class Servicio(models.Model):
    servicioNombre = models.CharField(max_length=200)
    #productoDescription = models.CharField(blank=True, max_length=200)
    #productoPrice = models.DecimalField(max_digits=10, decimal_places=2)
    #productoImage = models.ImageField(null=True, blank=True, upload_to='images/')
    # create_at = models.DateTimeField(default=datetime.datetime.now)
    def __str__ (self):
        return self.servicioNombre



#---Ticket------------------------------------------------------------------------------------------------
class Ticket(models.Model) :
    nroticket = models.CharField(max_length=200)
    fechayhora= models.DateTimeField(default=datetime.datetime.now)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE, verbose_name='Cliente', null=False)
    cajero = models.ForeignKey(Cajero,on_delete=models.CASCADE, verbose_name='Cajero', null=False)
    tipoAtencion = models.ForeignKey(TipoAtencion,on_delete=models.CASCADE, verbose_name='Tipoatencion', null=False)
    sucursal = models.ForeignKey(Sucursal,on_delete=models.CASCADE, verbose_name='Sucursal', null=False)
    caja = models.ForeignKey(Caja,on_delete=models.CASCADE, verbose_name='Caja', null=False)
    
    def ticket_completo(self):
        return "ticket-{}".format(self.nroticket)
    
    def __str__(self):
        return self.ticket_completo()
    
    #def __str__ (self):
     #    return '{0}'.format(self.id)



#---TicketServicio------------------------------------------------------------------------------------------------
class TicketServicio(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, verbose_name='Ticket', null=False)
    servicio = models.ForeignKey(Servicio,on_delete=models.CASCADE, verbose_name='Servicio requerido', null=False)
    #cantidad = models.PositiveIntegerField(default=0)
    #preciounit = models.FloatField()
    #modified = models.DateTimeField(auto_now=True)
    #created_at = models.DateTimeField(auto_now_add=True)
    #state = models.BooleanField(default = True)
    
    def __str__(self):
        return f'{self.ticket} solicito {self.servicio}'

    class Meta:
        indexes = [
                models.Index(fields=['ticket', 'servicio',]),
            ]

  