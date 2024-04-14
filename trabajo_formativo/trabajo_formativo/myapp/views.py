
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages

from django.contrib.auth.decorators import login_required





def registro(request):
    if request.method == 'GET':
        return render(request, 'Registro.html')
    else:
        if request.POST["claveusuario1"] == request.POST["claveusuario2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["nombreusuario"],
                    first_name=request.POST["nombres"],
                    last_name=request.POST["apellidos"],
                    email=request.POST["correoelectronico"],
                    password=request.POST["claveusuario1"]
                )
                user.save()
                login(request, user)
                return redirect('login')
            except IntegrityError:
                return render(request, 'Registro.html', {"error": "Username already exists."})
        else:
            return render(request, 'Registro.html', {"error": "Passwords did not match."})



def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'login.html', {"form": AuthenticationForm()})
    else:
        nombreusuario = request.POST['nombreusuario']
        claveusuario1 = request.POST['claveusuario1']
        
        try:
            user = User.objects.get(username=nombreusuario)
        except User.DoesNotExist:
            messages.add_message(request, messages.ERROR, 'Usuario no existe')
            return redirect('login.html')
        
        user = authenticate(request, username=nombreusuario, password=claveusuario1)
        
        if user is None:
            messages.add_message(request, messages.ERROR, 'Usuario o contraseña incorrecta')
            return redirect('login.html')
        
        login(request, user)
        
        
        if user.is_staff:
            return redirect('usuarioadmin')  
        else:
            return redirect('usuario') 


    


@login_required
def modificar(request):
    user = request.user

    if request.method == 'GET':
        data = {
            'nombreusuario': user.username,
            'nombres': user.first_name,
            'apellidos': user.last_name,
            'correoelectronico': user.email
        }
        return render(request, 'ModificarDatos.html', data)

    else:
        nombres = request.POST["nombres"]
        apellidos = request.POST["apellidos"]
        correoelectronico = request.POST["correoelectronico"]

        if not nombres or not apellidos or not correoelectronico:
            messages.error(request, 'Todos los campos son requeridos.')
            return redirect('modificar')

        user.first_name = nombres
        user.last_name = apellidos
        user.email = correoelectronico

        try:
            user.save()
            messages.success(request, 'Datos actualizados correctamente.')
            return redirect('usuario')  
        except:
            messages.error(request, 'Error al actualizar datos.')
            return redirect('modificar')



@login_required
def eliminar_cuenta(request):
    if request.method == 'GET':
        return render(request, 'eliminar_Cuenta.html')
    
    elif request.method == 'POST':
        user = request.user
        password = request.POST.get('password', '')

        
        if user.check_password(password):
            user.delete()
            logout(request)
            messages.success(request, 'Tu cuenta ha sido eliminada correctamente.')
            return redirect('login')
        else:
            messages.error(request, 'La contraseña es incorrecta. Inténtalo de nuevo.')
            return redirect('eliminar_cuenta')



    
    

def index(request):
    return render(request, "index.html")



def salir(request):
 
    return redirect('salir.html')



def Accion(request):
         
    return render(request, 'Accion.html')


def Deporte(request):
    return render(request, 'Deporte-baile.html')

def Disparos(request):
    return render(request, 'Disparos.html')

def Rol(request):
    return render(request, 'Rol-RPG.html')

def Terror(request):
    return render(request, 'Terror.html')


def usuario(request):
    return render(request, 'usuario1.html')


def usuarioadmin(request):
    return render(request, 'usuarioadmin.html')