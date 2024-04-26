from django.db import models

# Create your models here.
# This model should only be created in Admin, it's inventory
class Item(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='ecommerce/image/', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title

# class ShoppingCart(models.Model):
#     cart_item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    