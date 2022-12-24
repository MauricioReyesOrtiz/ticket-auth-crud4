from rest_framework import serializers
from api.models import Cliente, Cajero, Sucursal, TipoAtencion, Caja, Servicio, Ticket, TicketServicio 
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token



class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'
        read_only_fields = ('created_at',)

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        
class CajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cajero
        fields = '__all__'


class TipoAtencionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAtencion
        fields = '__all__'
        
        
        
class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = '__all__'
        
        
        
class CajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caja
        fields = '__all__'


#ticket roba
class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
        extra_kwargs = {
            'fechayhora': {'read_only': True, 'required': False},
            # 'fecha': {'read_only': True},
        }        
        
#tercer tabla
class TicketServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketServicio
        fields = '__all__'


#usuario no tocar
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'groups', 'email']
         #esconder password
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user