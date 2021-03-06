from django.urls import path
from django.contrib.auth.views import login, logout_then_login
from usuario import views


urlpatterns = [
    ##Usuario##
    path('registrar/', views.RegistrarUsuarioView.as_view() , name = 'registrar'),
    path('login/', login, {'template_name': 'login2.html'}, name='login'),
    path('logout/', logout_then_login, {'login_url': 'login'},name= 'logout'),
]