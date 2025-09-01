from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def superuser_required(view_func):
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_superuser:
            return render(request, 'admin_panel/403.html', status=403)
        return view_func(request, *args, **kwargs)
    return _wrapped_view
