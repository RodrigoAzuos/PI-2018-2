from django.shortcuts import render
from django.views.generic.base import View
from usuario.forms import RegistrarUsuarioForm
from django.contrib.auth.models import User
from comum.models import Perfil
from django.shortcuts import redirect


# Create your views here.

class RegistrarUsuarioView(View):

    def get(self, request):
        return render(request, 'registrar.html')

    def post(self, request):
        form = RegistrarUsuarioForm(request.POST)
        print(form.data)

        if (form.is_valid()):
            dados = form.data


            usuario = User.objects.create_user(username=dados['usuario'],
                                                    first_name=dados['first_name'],
                                                    last_name=dados['last_name'],
                                                    email=dados['email'],
                                                    password=dados['senha'])

            perfil = Perfil(sexo=dados['sexo'],
                        telefone=dados['telefone'],
                        data_nascimento=dados['data_nascimento'],
                        usuario=usuario)
            perfil.save()
            return redirect('index')

        return render(request, 'registrar.html', {'form': form})
