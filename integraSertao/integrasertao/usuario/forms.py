# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User



class RegistrarUsuarioForm(forms.Form):

    usuario = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    senha = forms.CharField(required=True)
    telefone = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    data_nascimento = forms.CharField(required=True)
    sexo = forms.CharField(required=True)



    def is_valid(self):
        valid = True

        if not super(RegistrarUsuarioForm, self).is_valid():
            self.adiciona_erro('Por favor, verifique os dados informados')
            valid = False

        user_exists = User.objects.filter(username=self.data['usuario']).exists()

        if user_exists:
            self.adiciona_erro('Usuario já existente')
            valid = False

        return valid

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)