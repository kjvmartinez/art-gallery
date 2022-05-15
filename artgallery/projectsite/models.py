from django.db import models

# Create your models here.
class Art(models.Model):
    name = models.CharField(max_length=120)
    size = models.CharField(max_length=120)
    style = models.CharField(max_length=120)
    painter = models.CharField(max_length=120)
    yearofcreation = models.CharField(max_length=4, verbose_name = "Year of Creation")
    artdescription =models.CharField(max_length=500, verbose_name = "Description")

    class Meta:
        verbose_name_plural = "Arts"

    def __str__(self):
        return self.name

