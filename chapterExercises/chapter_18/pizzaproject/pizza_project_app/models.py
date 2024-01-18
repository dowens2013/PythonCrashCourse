from django.db import models


class Pizza(models.Model):
    """Pizza"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """return string of model"""
        return self.text


class Topping(models.Model):
    """Toppings for the pizza"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        """return a string representing the entry"""
        return self.name

