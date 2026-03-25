from django.db import models

CATEGORY_CHOICES = [
    ('Men', 'Men'),
    ('Women', 'Women'),
    ('Kids', 'Kids'),
    ('Sports', 'Sports'),
    ('Casual', 'Casual'),
    ('Formal', 'Formal'),
    ('Boots', 'Boots'),
]

class Shoe(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='shoes/')
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='Men'  # default avoids migration errors
    )

    def __str__(self):
        return self.name

class CustomerQuery(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name