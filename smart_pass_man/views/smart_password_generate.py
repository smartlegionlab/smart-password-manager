from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from smart_pass_man.forms.secret_phrase_form import SecretPhraseForm
from smart_pass_man.models import SmartPassword
from smart_pass_man.services import SmartPasswordService


@login_required
@login_required
def smart_password_generate_view(request, smart_pass_id):
    try:
        smart_password = SmartPassword.objects.get(id=smart_pass_id, user=request.user)

        if request.method == 'POST':
            form = SecretPhraseForm(request.POST)
            if form.is_valid():
                secret_phrase = form.cleaned_data['secret_phrase']
                password = SmartPasswordService.generate_password(smart_pass_id, request.user, secret_phrase)

                request.session['password'] = password
                messages.success(request, 'Smart Password generated successfully!')
                return redirect('smart_password_manager:smart_password_list')
        else:
            form = SecretPhraseForm()

        context = {
            'form': form,
            'smart_password': smart_password,
            'active_page': 'manager',
        }
        return render(request, 'smart_pass_man/secret_phrase_form.html', context)

    except SmartPassword.DoesNotExist:
        messages.error(request, 'Smart password not found')
        return redirect('smart_password_manager:smart_password_list')
    except ValidationError as e:
        messages.error(request, e.messages[0])
        return redirect('smart_password_manager:smart_password_list')