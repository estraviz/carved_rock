from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    stock_count = models.IntegerField(help_text="How many items are currently in stock.")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(default="", blank=True)
    sku = models.CharField(max_length=20, unique=True, verbose_name="stock keeping unit")

    class Meta:
        ordering = ['price', 'name']
        constraints = [
            models.CheckConstraint(check=models.Q(price__gte=0), name="price_not_negative")
        ]

    def __str__(self):
        return self.name


class ProductImage(models.Model):  # one-to-many relationship
    image = models.ImageField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str(self):
        return self.image


class Category(models.Model):  # many-to-many relationship
    name = models.CharField(max_length=100)
    products = models.ManyToManyField('Product')

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self) -> str:
        return self.name
