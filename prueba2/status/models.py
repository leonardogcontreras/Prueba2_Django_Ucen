from django.db import models

class Status(models.Model):
    status = models.CharField(max_length=50, null=False, blank=True)

    def __str__(self):
       return self.status
