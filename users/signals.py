from django.db.models.signals import pre_delete
from django.dispatch import receiver
from users.models import User


@receiver(pre_delete, sender=User)
def user_delete_handler(sender, instance, **kwargs):
    instance.avatar.delete(save=False)
