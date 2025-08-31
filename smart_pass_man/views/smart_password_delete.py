from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import redirect

from smart_pass_man.services import SmartPasswordService


@login_required
def smart_password_delete_view(request, smart_pass_id):
    try:
        SmartPasswordService.delete_smart_password(smart_pass_id, request.user)
        messages.success(request, 'Smart Password deleted successfully!')
    except ValidationError as e:
        messages.error(request, e.messages[0])
    except Exception as e:
        print(e)
        messages.error(request, 'Error deleting smart password')
    return redirect('smart_password_manager:smart_password_list')
