from django.db import models

# Create your models here.


class Algorithme(models.Model):
    ALGO = (
        ('GD','GD'),
        ('GS','GS'),
    )
    Ram = models.FloatField(null=True)
    Poids = models.FloatField(null=True)
    Touchscreen = models.FloatField(null=True)
    Pixels_par_pouce = models.FloatField(null=True)
    HDD = models.FloatField(null=True)
    SDD = models.FloatField(null=True)
    algo = models.CharField(max_length=190, null=True, choices=ALGO)

    
