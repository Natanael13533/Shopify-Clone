from django.db import models

# Create your models here.
class Country(models.Model):
    code = models.CharField(max_length=40)
    name = models.CharField(max_length=100)
    tax = models.DecimalField(max_digits=5, decimal_places=2)
    tax_name = models.CharField(max_length=30, null=True, blank=True)

class Province(models.Model):
    TAX_TYPE_CHOICES = [('null', 'null'), ('normal', 'normal'), ('harmonized', 'harmonized'), ('compounded', 'compounded')]
    
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    code = models.CharField(max_length=40)
    name = models.CharField(max_length=100)
    tax = models.DecimalField(max_digits=5, decimal_places=2)
    tax_name = models.CharField(max_length=30, null=True, blank=True)
    tax_type = models.CharField(max_length=40, choices=TAX_TYPE_CHOICES, default='null')

    @property
    def tax_precentage(self):
        return int(self.tax * 100);