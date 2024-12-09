from django.db import models

from django.db import models
from django.contrib.auth.models import User

class IceCream(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2) 
    image_url = models.URLField()  
    
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  
    def __str__(self):
        return f"Cart of {self.user.username}"

    
    def get_total_price(self):
        return sum(item.get_total_price() for item in self.cart_items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.CASCADE) 
    ice_cream = models.ForeignKey(IceCream, on_delete=models.CASCADE)  
    quantity = models.PositiveIntegerField(default=1)  
    
    def __str__(self):
        return f"{self.quantity} x {self.ice_cream.name}"


    def get_total_price(self):
        return self.ice_cream.price * self.quantity

