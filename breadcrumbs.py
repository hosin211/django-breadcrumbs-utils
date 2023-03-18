__all__ = ['custom_path']

from functools import wraps

from django.urls import path


def custom_path(route, view, name=None, breadcrumb=None):
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        context = {'breadcrumb': breadcrumb}
        response = view(request, *args, **kwargs)
        if hasattr(response, "context_data"):
            response.context_data.update(context)
        return response

    return path(route, wrapper, name=name)
