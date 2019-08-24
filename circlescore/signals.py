from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

from circlescore.models import HikayaUser


@receiver(post_save, sender=User)
def create_hikaya_user(sender, instance, created, **kwargs):
    if created:
        HikayaUser.objects.create(
            user=instance,
            name='{} {}'.format(instance.first_name, instance.last_name)
        )


@receiver(post_save, sender=User)
def save_hikaya_user(sender, instance, **kwargs):
    instance.hikaya_user.save()


