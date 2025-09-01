from django.shortcuts import render

from admin_panel.decorators.superuser import superuser_required
from auth_logs.models import UserAuthLog
from core.utils.paginators import CachedCountPaginator


@superuser_required
def auth_log_list_view(request, pk):
    auth_log_list = UserAuthLog.objects.filter(user_id=pk)
    auth_log_count = auth_log_list.count()
    paginator = CachedCountPaginator(auth_log_list, 10, auth_log_count)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'active_page': "logs",
        'has_logs': auth_log_count > 0,
        'log_count': auth_log_count,
    }
    return render(request, 'admin_panel/users/user_auth_log_list.html', context)