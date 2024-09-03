from django.db import models

# Create your models here.
class Recipe(models.Model):
    # 1 oz = 28.35 grams
    # 1 liter =  33.814 ounnces 
    # 1 cup = 8 ounces
    # 1 glass = 8 oounces
    MEASURE = (
        ('OZ','ounces'),
        ('GM', 'grams'),
        ('L','liters'),
        ('LB', 'pounds'),
        ('CUP', 'cups'),
        ('DR', 'drams'),
        
    )
    name = models.CharField(max_length = 255)
    measure = models.CharField(max_length = 20, choices = MEASURE, default = 'ounces' )


    pass
