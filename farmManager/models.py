from django.db import models

# Create your models here.

class records(models.Model):
    pen_no = models.CharField(max_length=100)
    production_type = models.CharField(max_length=200)
    date_received = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField(null=True)
    no_birds = models.IntegerField(null=True)
    feed = models.IntegerField(null=True)
    egg_production = models.IntegerField(null=True)
    total_stock = models.IntegerField(null=True)
    medication = models.CharField(max_length=700)
    remarks = models.CharField(max_length=700)

    def __str__(self):
        return self.remarks
