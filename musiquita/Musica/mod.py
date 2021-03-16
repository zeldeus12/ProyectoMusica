from django.db import models
from django.conf import settings

class audi(models.Model):
    usuariocreatedor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='usercreacion')

    class Meta:
        abstract = True
