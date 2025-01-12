from django.db import models
from django.utils import timezone
# Create your models here.
class chaiVariety(models.Model):
    
    name = models.CharField(max_length=50) 
    image=models.ImageField(upload_to='images/')
    date_added = models.DateTimeField(default=timezone.now)
    chai_type_choice = [
        ('mc','masala chai'),
        ('gc','ginger chai'),
        ('ec','elaichi chai'),
    ] 
    type=models.CharField(max_length=2,choices=chai_type_choice)
    description= models.TextField(default='description')
    
    def __str__(self):
        return self.name