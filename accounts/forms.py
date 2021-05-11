from django import forms
from django.contrib.auth import authenticate, login
from accounts.models import User

class SignInForm(forms.Form):

    username = forms.CharField(
        max_length = 255,
        required = True,
        widget = forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder': 'Ingresar su email'
            }
        ),
        error_messages = {'required': 'Requerido'},
        label = 'Usuario'
    )

    password = forms.CharField(
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Ingresar su contraseña'
            }
        ),
        error_messages = {'required': 'Requerido'},
        label = 'Contraseña'
    )

    def clean(self):

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:

            if User.objects.filter(username=username).exists():

                auth = authenticate(username=username, password=password)

                if auth is None:
                    self.add_error('password', 'Contraseña inválida')

            else:
                self.add_error('username', 'Usuario no registrado')

    def login(self, request):

        username = self.cleaned_data.get('username')

        if User.objects.filter(
            username = username
            ).exists():

            user = User.objects.get(username=username)
        else:
            user = None

        return user
