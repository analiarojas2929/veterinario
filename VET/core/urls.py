from django.urls import include, path
from django.urls import path,include
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.index, name=('index')),
    path('index',views.index, name=('index')),
    path('servicio',views.servicio,name=('servicio')),
    path('inicio',views.inicio,name=('inicio')),
    path('galeria',views.galeria,name=('galeria')),
    path('somos',views.somos,name=('somos')),
    path('accounts/', include('django.contrib.auth.urls')),
    path("registro/",views.registro, name="registro"),
    path('formulario',views.formulario,name=('formulario')),
    
    

]
