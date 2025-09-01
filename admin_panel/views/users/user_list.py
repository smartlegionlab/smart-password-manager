from django.shortcuts import render

from admin_panel.decorators.superuser import superuser_required
from core.utils.paginators import CachedCountPaginator
from users.models import User


@superuser_required
def user_list_view(request):
    user_list = User.objects.all()
    user_count = user_list.count()
    paginator = CachedCountPaginator(user_list, 100, user_count)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'user_count': user_count,
        'has_users': user_count > 0,
    }
    return render(request, 'admin_panel/users/admin_user_list.html', context)