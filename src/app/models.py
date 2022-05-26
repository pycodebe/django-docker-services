from django.db import models

class Car(models.Model):
    model = models.CharField(max_length=60)
    brand = models.CharField(max_length=60)    

    class Meta:
        db_table = 'cars'

    def __str__(self):
        return self.model