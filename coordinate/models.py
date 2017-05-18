from django.db import models


class Transfer(models.Model):
    origin_phone = models.CharField(max_length=50)
    publish_time = models.DateTimeField()
    token = models.CharField(max_length=50, null=True)
    share_pin = models.IntegerField()
    data_type = models.IntegerField(null=True)
    related_data = models.CharField(max_length=5000, null=True)
    ip = models.CharField(max_length=30, null=True)
    ip_direct = models.CharField(max_length=30, null=True)
    port = models.IntegerField(null=True)
    is_active = models.BooleanField()

