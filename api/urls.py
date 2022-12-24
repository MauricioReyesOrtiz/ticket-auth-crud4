from rest_framework import routers
from api.views import ClienteViewSet, CajeroViewSet, SucursalViewSet, TipoAtencionViewSet, CajaViewSet, ServicioViewSet, TicketViewSet, TicketServicioViewSet,UserViewSet, LogoutView , LoginView
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
router  = routers.DefaultRouter()

#-------------------------------------------------------------------------------------------
router.register('cliente', ClienteViewSet)
router.register('cajero', CajeroViewSet)
router.register('sucursal', SucursalViewSet)
router.register('tipoatencion', TipoAtencionViewSet)
router.register('caja', CajaViewSet)
router.register('servicio', ServicioViewSet)
router.register('ticket', TicketViewSet)
router.register('ticketservicio', TicketServicioViewSet)
router.register('user', UserViewSet)


#---ESTO DE ABAJO NO TOCAR-------------------------------------------------------------
urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
] + router.urls