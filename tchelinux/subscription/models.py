from django.db import models

from tchelinux.core.models import AbstractBaseModel


class Subscription(AbstractBaseModel):

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'

    event = models.ForeignKey('event.Event', verbose_name='Evento', on_delete=models.CASCADE)
    fullname = models.CharField(verbose_name='Título', max_length=255)
    email = models.EmailField(verbose_name='E-mail', max_length=255)

    def __str__(self):
        return self.fullname
