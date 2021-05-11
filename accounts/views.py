from django.shortcuts import render
from django.contrib.auth import login, logout
from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.serializers import MyTokenObtainPairSerializer
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView
from django.contrib import messages

# forms
from accounts.forms import SignInForm


# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class SignIn(FormView):

    form_class = SignInForm
    success_url = '/'
    template_name = 'sign-in.html'

    def form_invalid(self, form):

        print ('form_invalid')

        if self.request.is_ajax():

            logout(self.request)

            return JsonResponse({
                'errors': form.errors
                }, status=400)
        else:
            return super(SignIn, self).form_invalid(form)

    def form_valid(self, form):

        try:
            logout(self.request)

            user = form.login(self.request)
            login(self.request, user)

            if self.request.is_ajax():

                return JsonResponse({
                    'status': True,
                    'data': {}
                })
            else:
                return HttpResponseRedirect('/')

        except:
            return render(self.request, '500.html', status=500)

@login_required
def user_profile(request):
    user=request.user
    if request.method == "POST":
        var_post = request.POST.copy()
        first_name = var_post['first_name']
        last_name = var_post['last_name']
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        messages.success(request, 'Datos personales cambiados correctamente')
    nombre = user.get_full_name()
    return render(request, 'profile.html', {
        'name':nombre,
        'first_name':user.first_name.capitalize(),
        'last_name':user.last_name.capitalize(),
        'email':user.email
    })

@login_required
def user_picture(request):
    user=request.user
    nombre = user.get_full_name()
    return render(request, 'picture.html', {
        'name':nombre,
        'first_name':user.first_name.capitalize(),
        'last_name':user.last_name.capitalize(),
        'email':user.email
    })
