from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods

from core.services.email_service import Email


@login_required
@require_http_methods(["POST"])
def user_delete_view(request):
    user = request.user
    email = user.email
    full_name = user.full_name
    
    try:
        msg = f"""Hey, {full_name}. I want to notify you,
        that your account was successfully deleted!"""
        
        Email.notification(
            to=email,
            title="Account deletion",
            message=msg,
        )
        
        user.delete()
        messages.success(request, 'Profile deleted successfully')
        
    except Exception as e:
        print(f"Error during account deletion for user {email}: {e}")
        messages.error(request, 'Something went wrong while deleting profile')
        return redirect('users:user_detail')
    
    return redirect('users:login')
