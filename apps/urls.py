from django.urls import path
from .views import (cargar_inicio, LoginView, LogoutView,TablaList,RegistrarTablaCreate)

urlpatterns = [
    path('', cargar_inicio, name = 'inicio'),
    path('informes/', TablaList.as_view(), name ='informacion'),
    path('iniciasesion/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('RegistroActividad/', RegistrarTablaCreate.as_view(), name = 'Registrar_Actividades'),
    path('logoutsesion/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    
]

