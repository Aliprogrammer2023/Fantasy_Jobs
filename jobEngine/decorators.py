from django.http import HttpResponseForbidden, HttpResponse


def authenticatedUser(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponse('Sorry! You have already logged in!!!')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args,**kargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name 
            if group in allowed_roles:
                return view_func(request,*args,**kargs)
            else:
                return HttpResponseForbidden('Sorry! But you are not allowed to view this page!')
        return wrapper_func
    return decorator 
