from django.db import models

# Create your models here.
class Ingredient(models.Model):
    '''
    MEASURE = (
        ('OZ','ounces'),
        ('GM', 'grams'),
        ('L','liters'),
        ('LB', 'pounds'),
        ('CUP', 'cups'),
        ('DR', 'drams'),
        
    )
    This is the ingredients list.
    '''
    name = models.CharField(max_length = 255, null = True, default = False) #Name of the ingredient.

    

    class Meta:
        
        ordering = ['-name']
        



    def __str__(self):
        return self.name

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
    name = models.CharField(max_length = 255) # Name of the recipe
    measure = models.CharField(max_length = 20, choices = MEASURE, default = 'ounces' )
    ingredient= models.ForeignKey(Ingredient, on_delete = models.CASCADE)
    

    class Meta:
        ordering = ['-name']
        verbose_name_plural = 'recipies'
    
    def __str__(self):
        return self.name
    

class Quantity(models.Model):
    pass



class Directions(models.Model):
                 
    pass

class Conversion(models.Model):
    pass 