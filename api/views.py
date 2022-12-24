from rest_framework import viewsets, permissions
from api.models import Cliente, Cajero, Sucursal, TipoAtencion, Caja, Servicio, Ticket, TicketServicio
from api.serializers import ClienteSerializer, CajeroSerializer, SucursalSerializer, TipoAtencionSerializer, CajaSerializer, ServicioSerializer, TicketSerializer, TicketServicioSerializer, UserSerializer
from rest_framework import status,views, response
from rest_framework import authentication
from django.contrib.auth.models import User
from django.contrib.auth import logout ,authenticate, login 
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

#-----------------------------------------------------------------------------------------------------------------------

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes = [authentication.BasicAuthentication]
    

class CajeroViewSet(viewsets.ModelViewSet):
  queryset = Cajero.objects.all()  
  permission_classes = [permissions.AllowAny]
  serializer_class = CajeroSerializer
  
class TipoAtencionViewSet(viewsets.ModelViewSet):
  queryset = TipoAtencion.objects.all()  
  permission_classes = [permissions.AllowAny]
  serializer_class = TipoAtencionSerializer


class SucursalViewSet(viewsets.ModelViewSet):
  queryset = Sucursal.objects.all()  
  permission_classes = [permissions.AllowAny]
  serializer_class = SucursalSerializer


class CajaViewSet(viewsets.ModelViewSet):
  queryset = Caja.objects.all()  
  permission_classes = [permissions.AllowAny]
  serializer_class = CajaSerializer
  
  
class ServicioViewSet(viewsets.ModelViewSet):
  queryset = Servicio.objects.all()  
  permission_classes = [permissions.AllowAny]
  serializer_class = ServicioSerializer
  

#esta tabla hacer Ticket
class TicketViewSet(viewsets.ModelViewSet):
  queryset = Ticket.objects.all()
  permission_classes = [permissions.IsAuthenticated] #aqui cambia-no tocar
  #permission_classes = [permissions.AllowAny]
  authentication_classes = [authentication.TokenAuthentication,]#aqui cambi-no tocar
  serializer_class = TicketSerializer


#esta tabla hacer TicketServicio
class TicketServicioViewSet(viewsets.ModelViewSet):
  queryset = TicketServicio.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = TicketServicioSerializer

#----NO TOCAR LO DE ABAJO-------------------------------------------------------------------------------------
class UserViewSet(viewsets.ModelViewSet):  #ReadOnlyModelViewSet
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser,]
    authentication_classes = [authentication.BasicAuthentication,]

class LoginView(views.APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        # Recuperamos las credenciales y autenticamos al usuario
        username2= request.data.get('username', None)
        password2 = request.data.get('password', None)
        if username2 is None or password2 is None:
            return response.Response({'message': 'Please provide both username and password'},status=status.HTTP_400_BAD_REQUEST)
        user2 = authenticate(username=username2, password=password2)
        if not user2:
            return response.Response({'message': 'Usuario o Contraseña incorrecto !!!! '},status=status.HTTP_404_NOT_FOUND)

        token, _ = Token.objects.get_or_create(user=user2)
        # Si es correcto añadimos a la request la información de sesión
        if user2:
            # para loguearse una sola vez
            # login(request, user)
            return response.Response({'message':'usuario y contraseña correctos!!!!'},status=status.HTTP_200_OK)
            #return response.Response({'token': token.key}, status=status.HTTP_200_OK)

        # Si no es correcto devolvemos un error en la petición
        return response.Response(status=status.HTTP_404_NOT_FOUND)        

class LogoutView(views.APIView):
    authentication_classes = [authentication.TokenAuthentication]
    def post(self, request):        
        request.user.auth_token.delete()
        # Borramos de la request la información de sesión
        logout(request)
        # Devolvemos la respuesta al cliente
        return response.Response({'message':'Sessión Cerrada y Token Eliminado !!!!'},status=status.HTTP_200_OK)
