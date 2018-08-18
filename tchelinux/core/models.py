from django.db import models
from django.utils import timezone

from tchelinux.core.signals import post_soft_delete
from tchelinux.core.manager import Manager


class AbstractBaseModel(models.Model):
    """Abstrate base model used by the apps of the MyreksAPI project.

    This model allows the implementation of logical exclusion.
    """
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    objects = Manager()

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()
        post_soft_delete.send(sender=type(self), instance=self, using=self._state.db)
