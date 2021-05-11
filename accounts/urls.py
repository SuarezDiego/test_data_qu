from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from accounts.views import SignIn, user_picture, user_profile

app_name = 'accounts'

urlpatterns = [
    # sign in
    path('sign-in/', SignIn.as_view(), name='sign_in'),

    # sign out
    path('sign-out/', auth_views.LogoutView.as_view(next_page='/'), name='sign_out'),

    # forgort
    path('forget/', TemplateView.as_view(template_name="forget.html"), name='forget'),

    path('profile',
        user_profile,
        name='profile'
    ),
    path('picture',
        user_picture,
        name='picture'
    ),
    path('changepassword',
        auth_views.PasswordChangeView.as_view(
            template_name="changepassword.html",
            success_url=reverse_lazy('accounts:change-password'),
        ),
        name='change-password'
    ),

    path('password_reset/', auth_views.PasswordResetView.as_view(
            success_url=reverse_lazy('accounts:password_reset_done'),
            template_name='login/password_reset_form.html',
            email_template_name='login/password_reset_email.html'
        ),
        name='password_reset'
    ),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
            template_name='login/password_reset_done.html'
        ),
        name='password_reset_done'
    ),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
            success_url=reverse_lazy('accounts:password_reset_complete'),
            template_name="login/password_reset_confirm.html"
        ),
        name='password_reset_confirm'
    ),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
            template_name='login/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ), 
    


]