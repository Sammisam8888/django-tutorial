from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import timedelta
# Create your models here.

# timezone.activate('Asia/Kolkata')
# Set the timezone to GMT +5:30 (Asia/Kolkata) - but its not required as its already defined in the settings.py file

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
    
#Foreign key reference relationship - one to many
class chaireview(models.Model):
    chai = models.ForeignKey(chaiVariety, on_delete=models.CASCADE, related_name='reviews') 
    #on delete cascade refers to the delete cascade feature in sql which means that when a chai is deleted, all the reviews associated with it will also be deleted.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    date_added = models.DateTimeField(default=timezone.now)
    review = models.TextField(default='review')

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    
#Many to many relationship
class Store(models.Model):
    chai_varieties = models.ManyToManyField(chaiVariety)  # Use one field
    store_name = models.CharField(max_length=50)  
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.store_name
 
#one to one relationship
class chaiCertificate(models.Model):
    chai = models.OneToOneField(
        chaiVariety, on_delete=models.CASCADE, related_name='certificate'
    )
    certificate = models.ImageField(upload_to='certificates/')
    certificate_number = models.CharField(max_length=50)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField(default=lambda: timezone.now() + timedelta(days=5*365))

    def __str__(self):
        return f'Certificate for {self.chai.name}'
