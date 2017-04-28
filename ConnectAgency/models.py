from django.db import models


class Transfer(models.Model):
    origin_phone = models.CharField(max_length=50)
    publish_time = models.DateTimeField()
