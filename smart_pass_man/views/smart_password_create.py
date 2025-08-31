from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from smart_pass_man.forms.smart_password_form import SmartPasswordForm
from smart_pass_man.services import SmartPasswordService


@login_required
def smart_password_create_view(request):
    if request.method == 'POST':
        form = SmartPasswordForm(request.POST)
        try:
            SmartPasswordService.create_smart_password(request.user, request.POST)
            messages.success(request, 'Smart Password created successfully!')
            return redirect('smart_password_manager:smart_password_list')
        except ValidationError as e:
            messages.error(request, e.messages[0])
        except Exception as e:
            print(e)
            messages.error(request, 'Error creating smart password')
    else:
        form = SmartPasswordForm()

    context = {
        'form': form,
        'active_page': 'manager',
    }
    return render(request, 'smart_pass_man/smart_password_form.html', context)