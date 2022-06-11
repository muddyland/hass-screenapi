from django.core.exceptions import PermissionDenied
from .settings import SECRET_KEY
def key_check(function):
    def wrap(request, *args, **kwargs):
      key = request.headers.get("AUTH")
      if key == SECRET_KEY:
        return function(request, *args, **kwargs)
      else:
        print("Key check failed")
        raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

