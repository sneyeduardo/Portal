from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from cursos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # --- AUTENTICACIÓN ---
    path('login/', auth_views.LoginView.as_view(template_name='cursos/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    
    # --- PORTAL DE VIDEOS ---
    path('', views.dashboard_cursos, name='dashboard'),
    path('curso/<int:curso_id>/clase/<int:clase_id>/', views.reproductor_clase, name='reproductor'),
    
    # --- CONTROLES DE ADMINISTRADOR ---
    path('clase/nueva/', views.crear_clase, name='crear_clase'),
    path('clase/editar/<int:clase_id>/', views.editar_clase, name='editar_clase'),
    path('clase/eliminar/<int:clase_id>/', views.eliminar_clase, name='eliminar_clase'),
]