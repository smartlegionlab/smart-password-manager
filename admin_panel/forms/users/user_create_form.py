from django.contrib.auth.forms import UserCreationForm

from admin_panel.forms.users.user_base_form import BaseAdminUserForm


class AdminUserForm(BaseAdminUserForm, UserCreationForm):

    class Meta(BaseAdminUserForm.Meta):
        pass
