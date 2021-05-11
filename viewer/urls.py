from django.urls import path
from django.contrib.auth.decorators import login_required
from accounts.decorators import validate_access
from .views import *

app_name = 'viewer'

urlpatterns = [
    # dashboard
    path('', validate_access()(Dashboard.as_view()), name='dashboard'),
]
