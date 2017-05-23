from django.db import models


class Transfer(models.Model):
    origin_phone = models.CharField(max_length=50)
    publish_time = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=50, null=True)
    share_pin = models.IntegerField()
    data_type = models.CharField(max_length=20, null=True)
    related_data = models.CharField(max_length=5000, null=True)
    ip = models.CharField(max_length=30, null=True)
    port = models.IntegerField(null=True)
    is_active = models.BooleanField()
    installation_origin = models.CharField(max_length=50, null=True)
    installation_target = models.CharField(max_length=50, null=True)

