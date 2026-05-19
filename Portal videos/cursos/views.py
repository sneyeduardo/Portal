from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required # <-- Esta es la que faltaba
from django.utils import timezone
from django.contrib import messages
from .models import Clase, Curso
from .forms import ClaseForm
@login_required(login_url='/login/')
def dashboard_cursos(request):
    clases = Clase.objects.all()
    # Le pasamos "ahora" a la plantilla para comparar fechas
    return render(request, 'cursos/dashboard.html', {
        'clases': clases,
        'ahora': timezone.now()
    })

@login_required(login_url='/login/')
def reproductor_clase(request, curso_id, clase_id):
    curso = get_object_or_404(Curso, id=curso_id)
    clase_actual = get_object_or_404(Clase, id=clase_id, curso=curso)
    
    # SEGURIDAD: Si un alumno intenta forzar la URL de un video que aún no se estrena
    if clase_actual.fecha_estreno > timezone.now():
        messages.warning(request, "Esta clase aún no está disponible.")
        return redirect('dashboard')
    
    todas_las_clases = Clase.objects.filter(curso=curso)
    
    return render(request, 'cursos/reproductor.html', {
        'curso': curso,
        'clase_actual': clase_actual,
        'todas_las_clases': todas_las_clases,
        'ahora': timezone.now()
    })
@staff_member_required(login_url='/login/')
def crear_clase(request):
    if request.method == 'POST':
        form = ClaseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Clase creada con éxito!")
            return redirect('dashboard')
    else:
        form = ClaseForm()
    return render(request, 'cursos/formulario_clase.html', {'form': form, 'accion': 'Crear'})

@staff_member_required(login_url='/login/')
def editar_clase(request, clase_id):
    clase = get_object_or_404(Clase, id=clase_id)
    if request.method == 'POST':
        form = ClaseForm(request.POST, instance=clase)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Clase actualizada con éxito!")
            return redirect('dashboard')
    else:
        form = ClaseForm(instance=clase)
    return render(request, 'cursos/formulario_clase.html', {'form': form, 'accion': 'Editar'})

@staff_member_required(login_url='/login/')
def eliminar_clase(request, clase_id):
    clase = get_object_or_404(Clase, id=clase_id)
    clase.delete()
    messages.success(request, "Clase eliminada permanentemente.")
    return redirect('dashboard')