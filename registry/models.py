from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

CHAR_MAX_LENGTH = 256


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name=_('user'),
        on_delete=models.CASCADE
    )

    country = models.CharField(_('country'), max_length=CHAR_MAX_LENGTH)
    state = models.CharField(_('state'), max_length=CHAR_MAX_LENGTH)
    city = models.CharField(_('city'), max_length=CHAR_MAX_LENGTH)
    cep = models.IntegerField(_('cep'))
    street = models.CharField(_('street'), max_length=CHAR_MAX_LENGTH)
    houseNumber = models.PositiveIntegerField(_('houseNumber'))
    complement = models.CharField(
        _('complement'),
        max_length=CHAR_MAX_LENGTH,
        null=True
    )

    cpf = models.IntegerField(_('cpf'))
    pis = models.IntegerField(_('pis'))


@receiver(post_save, sender=User)
def createUserProfile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
