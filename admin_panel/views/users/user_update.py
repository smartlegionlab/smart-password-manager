from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from admin_panel.decorators.superuser import superuser_required
from admin_panel.forms.users.user_update_form import AdminUserUpdateForm
from users.models import User


@superuser_required
def user_update_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    original_password = user.password

    if request.method == 'POST':
        form = AdminUserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            user_profile = form.save(commit=False)

            new_password = form.cleaned_data.get('password')

            if new_password and new_password.strip():
                user_profile.set_password(new_password)
            else:
                user_profile.password = original_password

            user_profile.is_superuser = user_profile.is_staff
            user_profile.save()

            messages.success(request, f'Profile updated: {user_profile.email}')
            return redirect('admin_panel:admin_user_detail', pk=user_profile.id)
        else:
            error_messages = [f"{field}: {error}"
                              for field, errors in form.errors.items()
                              for error in errors]
            messages.error(request, ' '.join(error_messages))
    else:
        form = AdminUserUpdateForm(instance=user)

    context = {
        'form': form,
        'user': user
    }

    return render(request, 'admin_panel/users/admin_user_form.html', context)
