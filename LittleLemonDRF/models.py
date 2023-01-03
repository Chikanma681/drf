from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class MenuItem(models.Model):
    # price = models.DecimalField(max_digits=6, decimal_places=2)
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    inventory = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.title

        