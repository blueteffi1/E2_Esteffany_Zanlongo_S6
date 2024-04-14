from django.urls import path
from .views import index,modificar,registro, eliminar_cuenta, Disparos, Terror, iniciar_sesion, Deporte, Rol, Accion, usuario, usuarioadmin
from django.contrib.auth import views as auth_views


urlpatterns = [
   
    


    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),



    path('', index, name='index'),
    path('index.html', index, name='index'),
    path('Registro.html', registro, name='registro'),
    path('Accion.html', Accion, name='Accion'),
    path('Deporte-baile.html', Deporte, name='Deporte'),
    path('Disparos.html', Disparos, name='Disparos'),
    path('Rol-RPG.html', Rol, name='Rol'),
    path('Terror.html', Terror, name='Terror'),
    path('usuario1.html',usuario, name='usuario'),
    path('login.html', iniciar_sesion, name='login'),
    path('usuarioadmin.html', usuarioadmin, name='usuarioadmin'),
    path('ModificarDatos.html', modificar, name='modificar'),
    path('eliminar_cuenta.html', eliminar_cuenta, name='eliminar_cuenta'),
    

    
    
    



]