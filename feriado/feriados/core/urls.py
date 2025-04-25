from django.urls import path
from . import views

urlpatterns = [
    path('',views.feriado),
    path('listar_feriados/', views.listar_feriados, name='listar_feriados'),
    path('adicionar_novos_feriados/', views.adicionar_feriado, name='add_feriado'),
    path('modificar_feriado/<int:feriado_id>', views.modificar_feriado, name='mod_feriado'),
]
