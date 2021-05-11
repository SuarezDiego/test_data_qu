from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied

def validate_access(permission=None):
    def _validate_access(function):
        def wrap(request, *args, **kwargs):
            if request.user.is_authenticated:
                if permission:
                    if request.user.has_perm(permission):
                        return function(request, *args, **kwargs)
                    else:
                        raise PermissionDenied
                else:
                    return function(request, *args, **kwargs)
            else:
                return HttpResponseRedirect('/sign-in/')
        return wrap
    return _validate_access
