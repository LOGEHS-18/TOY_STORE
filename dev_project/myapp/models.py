from django.db import models

class User(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.username

# action_figures/models.py

from django.db import models

class ActionFigure(models.Model):
    CATEGORY_CHOICES = [
        ('Action Figures', 'Action Figures'),
    ]
    
    SUBCATEGORY_CHOICES = [
        ('Superheroes', 'Superheroes'),
        ('Movie Characters', 'Movie Characters'),
        ('Historical Figures', 'Historical Figures'),
    ]
    
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    subcategory = models.CharField(max_length=255, choices=SUBCATEGORY_CHOICES, blank=True, null=True)
    company = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()

    def __str__(self):
        return self.name

class BuildingToys(models.Model):
    CATEGORY_CHOICES = [
        ('Building Toys', 'Building Toys'),
    ]
    
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    company = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()

    def __str__(self):
        return self.name

class EducationalToys(models.Model):
    CATEGORY_CHOICES = [
        ('Educational Toys', 'Educational Toys'),
    ]
    
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    company = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()

    def __str__(self):
        return self.name

class DollsAndStuffedAnimals(models.Model):
    CATEGORY_CHOICES = [
        ('Dolls and Stuffed Animals', 'Dolls and Stuffed Animals'),
    ]
    
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    company = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()

    def __str__(self):
        return self.name

class GamesAndPuzzles(models.Model):
    CATEGORY_CHOICES = [
        ('Games and Puzzles', 'Games and Puzzles'),
    ]
    
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    company = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()

    def __str__(self):
        return self.name

class OutdoorToys(models.Model):
    CATEGORY_CHOICES = [
        ('Outdoor Toys', 'Outdoor Toys'),
    ]
    
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    company = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()

    def __str__(self):
        return self.name

class PretendPlayToys(models.Model):
    CATEGORY_CHOICES = [
        ('Pretend Play Toys', 'Pretend Play Toys'),
    ]
    
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    company = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()

    def __str__(self):
        return self.name

class CreativeAndArtToys(models.Model):
    CATEGORY_CHOICES = [
        ('Creative and Art Toys', 'Creative and Art Toys'),
    ]
    
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    company = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()

    def __str__(self):
        return self.name

class ElectronicToys(models.Model):
    CATEGORY_CHOICES = [
        ('Electronic Toys', 'Electronic Toys'),
    ]
    
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    company = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()

    def __str__(self):
        return self.name
class Admin(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email

class Product(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()

    def __str__(self):
        return self.name

class Cart(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.URLField()

    def __str__(self):
        return self.name

class Order(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    taxes = models.DecimalField(max_digits=10, decimal_places=2)
    final_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.id

class OrderItem(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.URLField()

    def __str__(self):
        return self.name
