from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.product.price * self.quantity

class Order(models.Model):
    items = models.ManyToManyField(OrderItem)
    ordered_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calculate_total(self):
        self.total_price = sum([item.get_total_price() for item in self.items.all()])
        self.save()
