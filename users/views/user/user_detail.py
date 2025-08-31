from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def user_detail_view(request):
    context = {
        'active_page': 'profile'
    }
    return render(request, 'users/user_detail.html', context)
