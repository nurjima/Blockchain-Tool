from django.db import models


class Blockchain(models.Model):
    address = models.CharField(max_length=100, null=False, blank=False)
    balance = models.BigIntegerField()

    def __str__(self):
        return self.address
