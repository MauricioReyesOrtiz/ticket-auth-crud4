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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication,]
    
    

class CajeroViewSet(viewsets.ModelViewSet):
  queryset = Cajero.objects.all()
  serializer_class = CajeroSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  authentication_classes = [authentication.BasicAuthentication,]
  
class TipoAtencionViewSet(viewsets.ModelViewSet):
  queryset = TipoAtencion.objects.all()
  serializer_class = TipoAtencionSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  authentication_classes = [authentication.BasicAuthentication,]


class SucursalViewSet(viewsets.ModelViewSet):
  queryset = Sucursal.objects.all()
  serializer_class = SucursalSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  authentication_classes = [authentication.BasicAuthentication,]


class CajaViewSet(viewsets.ModelViewSet):
  queryset = Caja.objects.all()
  serializer_class = CajaSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  authentication_classes = [authentication.BasicAuthentication,]
  
  
class ServicioViewSet(viewsets.ModelViewSet):
  queryset = Servicio.objects.all()
  serializer_class = ServicioSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  authentication_classes = [authentication.TokenAuthentication,]
  

#esta tabla hacer Ticket
class TicketViewSet(viewsets.ModelViewSet):
  queryset = Ticket.objects.all()
  serializer_class = TicketSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  authentication_classes = [authentication.TokenAuthentication,]
  


#esta tabla hacer TicketServicio
class TicketServicioViewSet(viewsets.ModelViewSet):
  queryset = TicketServicio.objects.all()
  serializer_class = TicketServicioSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  authentication_classes = [authentication.TokenAuthentication,]
  
  

#----NO TOCAR LO DE ABAJO-------------------------------------------------------------------------------------
class UserViewSet(viewsets.ModelViewSet):  #ReadOnlyModelViewSet
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser,]
    authentication_classes = [authentication.TokenAuthentication,]

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
            return response.Response({'message': 'Usuario o Contrase??a incorrecto !!!! '},status=status.HTTP_404_NOT_FOUND)

        token, _ = Token.objects.get_or_create(user=user2)
        # Si es correcto a??adimos a la request la informaci??n de sesi??n
        if user2:
            # para loguearse una sola vez
            # login(request, user)
            return response.Response({'message':'usuario y contrase??a correctos!!!!'},status=status.HTTP_200_OK)
            #return response.Response({'token': token.key}, status=status.HTTP_200_OK)

        # Si no es correcto devolvemos un error en la petici??n
        return response.Response(status=status.HTTP_404_NOT_FOUND)        

class LogoutView(views.APIView):
    authentication_classes = [authentication.TokenAuthentication]
    def post(self, request):        
        request.user.auth_token.delete()
        # Borramos de la request la informaci??n de sesi??n
        logout(request)
        # Devolvemos la respuesta al cliente
        return response.Response({'message':'Sessi??n Cerrada y Token Eliminado !!!!'},status=status.HTTP_200_OK)
