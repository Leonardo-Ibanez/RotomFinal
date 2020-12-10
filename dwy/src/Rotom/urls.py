
from django.contrib import admin
from django.urls import path, include
from sistema import views
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('nuevo_cliente.html/',views.nuevo_cliente, name="nuevo_cliente.html"),
    path('calculadora.html/', views.calculadora, name="calculadora"),
    path('crear_cliente.html/', views.crear_cliente, name = "crear_cliente.html"),
    path('listar_cliente.html/', views.listar_cliente, name = "listar_cliente.html"),
    path('listar_pedidos.html/', views.listar_pedidos, name = "listar_pedidos.html"),
    path('modificar_pedidos.html/<id>/', views.modificar_pedidos, name = "modificar_pedidos.html"),
    path('nuevo_pedido.html/', views.nuevo_pedido, name = "nuevo_pedido"),
    path('eliminar_pedidos.html/<id>/', views.eliminar_pedidos, name = "eliminar_pedidos.html"),
    path('accounts/', include ('django.contrib.auth.urls')),
    path('registrar.html/', views.registrar, name = "registrar"),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('logout', views.logout),
    path('ubicacion.html/', views.ubicacion, name = "ubicacion"),
    path('', include('pwa.urls')),

]
