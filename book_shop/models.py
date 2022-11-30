from django.db import models

class Post(models.Model):
    title = models.TextField(max_length=50)
    category = models.TextField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=5)
    published = models.DateTimeField(auto_now_add=True)


