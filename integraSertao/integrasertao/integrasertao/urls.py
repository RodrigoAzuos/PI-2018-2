"""integrasertao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from comum import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuario.urls')),
    path('', views.index, name='index'),
    path('add-post/', views.add_post, name='add-post'),
    path('post/<int:post_id>/', views.exibir_post, name='exibir_post'),
    path('categoria/<int:categoria_id>/', views.filtrar_categoria, name='filtrar'),
    path('buscar/<slug:palavra_chave>/', views.buscar, name='buscar'),
    # re_path(r'^buscar/(?P<palavra_chave>\w+)/$', views.buscar, name='buscar'),

]

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)

