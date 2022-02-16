from django.db import models


class Device(models.Model):
    device = models.TextField(default="")


class Type(models.Model):
    type = models.TextField(default="")


class Point(models.Model):
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)
    value = models.FloatField()
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE)
    time = models.DateTimeField()
