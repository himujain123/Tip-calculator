from django.db import models

class TipCalculation(models.Model):
	bill_amount = models.DecimalField(max_digits=10, decimal_places=2)
	tip_percentage = models.DecimalField(max_digits=5, decimal_places=2)
	num_people = models.IntegerField()
	tip_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
	total_amount_per_person = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

# Create your models here.
