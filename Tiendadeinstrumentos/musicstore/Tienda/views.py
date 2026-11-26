
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# ==========================================
# REGISTRO DE USUARIOS
# ==========================================

def registro(request):

    if request.user.is_authenticated:
        return redirect('inicio')

    if request.method == 'POST':

        nombre = request.POST.get('nombre', '').strip()
        correo = request.POST.get('correo', '').strip().lower()
        password = request.POST.get('password', '')
        confirmar = request.POST.get('confirmar', '')

        if not nombre or not correo or not password or not confirmar:
            messages.error(request, 'Completa todos los campos.')
            return render(request, 'tienda/registro.html')

        if User.objects.filter(username=correo).exists():
            messages.error(request, 'Este correo ya está registrado.')
            return render(request, 'tienda/registro.html')

        if User.objects.filter(email__iexact=correo).exists():
            messages.error(request, 'Este correo ya está registrado.')
            return render(request, 'tienda/registro.html')

        if password != confirmar:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'tienda/registro.html')

        if len(password) < 8:
            messages.error(
                request,
                'La contraseña debe tener al menos 8 caracteres.'
            )
            return render(request, 'tienda/registro.html')

        # Crear usuario y guardar sus datos en la base de datos.
        usuario = User.objects.create_user(
            username=correo,
            email=correo,
            password=password,
            first_name=nombre
        )

        # Iniciar sesión automáticamente después del registro.
        login(request, usuario)

        messages.success(
            request,
            f'¡Bienvenido a MusicStore, {nombre}!'
        )

        return redirect('inicio')

    return render(request, 'tienda/registro.html')


# ==========================================
# INICIO DE SESIÓN
# ==========================================

def iniciar_sesion(request):

    if request.user.is_authenticated:
        return redirect('inicio')

    if request.method == 'POST':

        correo = request.POST.get('correo', '').strip().lower()
        password = request.POST.get('password', '')

        usuario = authenticate(
            request,
            username=correo,
            password=password
        )

        if usuario is not None:

            login(request, usuario)

            return redirect('inicio')

        messages.error(
            request,
            'Correo o contraseña incorrectos.'
        )

    return render(request, 'tienda/login.html')


# ==========================================
# CERRAR SESIÓN
# ==========================================

def cerrar_sesion(request):

    if request.method == 'POST':
        logout(request)
        return redirect('login')

    return redirect('inicio')


# ==========================================
# PÁGINA DE INICIO
# ==========================================

@login_required(login_url='login')
def inicio(request):
    return render(request, 'tienda/index.html')


# ==========================================
# CATEGORÍAS
# ==========================================

@login_required(login_url='login')
def categorias(request):
    return render(request, 'tienda/categorias.html')


# ==========================================
# INSTRUMENTOS DE VIENTO
# ==========================================

@login_required(login_url='login')
def viento(request):

    instrumentos = [
        {
            'nombre': 'Saxofón Yamaha',
            'marca': 'Yamaha',
            'precio': 18500,
        },
        {
            'nombre': 'Tuba Yamaha',
            'marca': 'Yamaha',
            'precio': 32000,
        },
        {
            'nombre': 'Trompeta',
            'marca': 'Yamaha',
            'precio': 14500,
        },
        {
            'nombre': 'Saxofón Alto',
            'marca': 'Selmer',
            'precio': 28000,
        },
    ]

    return render(request, 'tienda/viento.html', {
        'instrumentos': instrumentos
    })


# ==========================================
# INSTRUMENTOS DE TECLADO
# ==========================================

@login_required(login_url='login')
def teclas(request):

    instrumentos = [
        {
            'nombre': 'Yamaha P-125',
            'marca': 'Yamaha',
            'precio': 18500,
        },
        {
            'nombre': 'Roland FP-30X',
            'marca': 'Roland',
            'precio': 22500,
        },
        {
            'nombre': 'Nord Stage 4',
            'marca': 'Nord',
            'precio': 68000,
        },
    ]

    return render(request, 'tienda/teclas.html', {
        'instrumentos': instrumentos
    })


# ==========================================
# INSTRUMENTOS DE CUERDA
# ==========================================

@login_required(login_url='login')
def cuerdas(request):

    instrumentos = [
        {
            'nombre': 'Gibson Les Paul Standard',
            'marca': 'Gibson',
            'precio': 58000,
        },
        {
            'nombre': 'Yamaha Pacifica',
            'marca': 'Yamaha',
            'precio': 12500,
        },
        {
            'nombre': 'Gibson Les Paul Custom',
            'marca': 'Gibson',
            'precio': 85000,
        },
    ]

    return render(request, 'tienda/cuerdas.html', {
        'instrumentos': instrumentos
    })


# ==========================================
# RECIBO DE COMPRA
# ==========================================

@login_required(login_url='login')
def comprar(request):

    nombre = request.GET.get('nombre', 'Instrumento')
    precio = request.GET.get('precio', '0')

    return render(request, 'tienda/recibo.html', {
        'nombre': nombre,
        'precio': precio,
    })

    
# ==========================================
# REGISTRO DE USUARIOS
# ==========================================

def registro(request):
    if request.user.is_authenticated:
        return redirect('inicio')

    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        correo = request.POST.get('correo', '').strip().lower()
        password = request.POST.get('password', '')
        confirmar = request.POST.get('confirmar', '')

        if not nombre or not correo or not password or not confirmar:
            messages.error(request, 'Completa todos los campos.')

        elif User.objects.filter(username=correo).exists():
            messages.error(request, 'Este correo ya está registrado.')

        elif User.objects.filter(email__iexact=correo).exists():
            messages.error(request, 'Este correo ya está registrado.')

        elif password != confirmar:
            messages.error(request, 'Las contraseñas no coinciden.')

        elif len(password) < 8:
            messages.error(
                request,
                'La contraseña debe tener al menos 8 caracteres.'
            )

        else:
            usuario = User.objects.create_user(
                username=correo,
                email=correo,
                password=password,
                first_name=nombre
            )

            login(request, usuario)
            messages.success(request, f'¡Bienvenido a MusicStore, {nombre}!')
            return redirect('inicio')

    return render(request, 'tienda/registro.html')


# ==========================================
# INICIAR SESIÓN
# ==========================================

def iniciar_sesion(request):
    if request.user.is_authenticated:
        return redirect('inicio')

    if request.method == 'POST':
        correo = request.POST.get('correo', '').strip().lower()
        password = request.POST.get('password', '')

        usuario = authenticate(
            request,
            username=correo,
            password=password
        )

        if usuario is not None:
            login(request, usuario)
            return redirect('inicio')

        messages.error(request, 'Correo o contraseña incorrectos.')

    return render(request, 'tienda/login.html')


# ==========================================
# CERRAR SESIÓN
# ==========================================

def cerrar_sesion(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    return redirect('inicio')
