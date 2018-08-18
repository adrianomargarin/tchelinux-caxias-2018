from django.db import models

from tchelinux.core.models import AbstractBaseModel


class Event(AbstractBaseModel):

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    title = models.CharField(verbose_name='Título', max_length=255)
    start_date = models.DateTimeField(verbose_name='Data de início')
    end_date = models.DateTimeField(verbose_name='Data de fim')
    location = models.CharField(verbose_name='Local', max_length=255)
    description = models.TextField(verbose_name='Descrição')

    def __str__(self):
        return self.title
